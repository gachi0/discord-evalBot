import discord
from discord.ext import commands as cmds
import toml
import subprocess as sbp
import os

config = toml.load(open("config.toml", encoding="utf-8"))
bot = cmds.Bot(
    command_prefix=config["prefix"],
    case_insensitive=True,
    intents=discord.Intents.default())


async def run(ctx: cmds.Context, text: str, cmd: str, exe=False):
    # 許可されている人でなければ帰る
    if ctx.author.id not in config["alloweds"]:
        await ctx.reply("許可されていません。")
        return
    # ソースコードのファイル名を格納する変数
    name = str(ctx.message.id)
    # 出力結果を格納する変数
    result = ""
    try:
        # ソースコードをファイルに書き込み
        with open(name, "w", encoding="utf-8") as f:
            f.write(text)
        # exeファイルが生成されるか(コンパイル言語か)どうか
        if exe:
            # まずexeを生成する
            result = sbp.getoutput([cmd, name])
            # exeの名前を保管
            exename = f"{name}.exe"
            # 正常にexeが生成されていたら
            if os.path.exists(exename):
                # 実行
                result = sbp.getoutput(exename)
                # exeファイルを消す
                os.remove(exename)
        else:
            # 出力を記録
            result = sbp.getoutput([cmd, name])
        # 出力結果を返信
        await ctx.reply(result if result != "" else "表示なし")
    except Exception as e:
        # エラーが発生していたらそれを送信
        await ctx.reply(f"エラー:\n{e}")
    # ソースコードファイルを消す
    os.remove(name)


@bot.command(aliases=["py"])
async def python(ctx: cmds.Context, *, text: str):
    await run(ctx, text, config["py"])


@bot.command(aliases=["js", "node"])
async def javascript(ctx: cmds.Context, *, text: str):
    await run(ctx, text, config["js"])


@bot.command(aliases=["cs", "c#", "csc"])
async def csharp(ctx: cmds.Context, *, text: str):
    await run(ctx, text, config["cs"], True)


@bot.command(aliases=["csi", "csharpi", "c#i"])
async def csharp_interactive(ctx: cmds.Context, *, text: str):
    await run(ctx, text, config["csi"])

bot.run(config["token"])
