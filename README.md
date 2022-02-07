# discord-evalBot
いろんな言語を走らせる

# セットアップ
## configの編集
`config.toml.sample`を`config.toml`にリネームします。    
tokenに、botのトークンを設定します。  
allowedsに、botのコマンドを使うことができる人のユーザーを配列形式で設定します。  
**これには、信用できる人のidのみを設定してください。  
botを動かすデバイス上で<u>任意のコードが実行</u>できるため、パスワードを盗むことや、プライベートな画像を覗き見することも容易にできます。**  
py, js, cs, csiには、それぞれ、自分の環境でそれらを動かすためのコマンド名、もしくはファイルパスを設定します。
## 必要なパッケージのインストール
`requirements.txt`と同じ場所で、以下のコマンドを実行します。  
```
pip install -r requirements.txt
```
## 実行
main.pyを実行します。  
```
python main.py
```

# コマンド一覧
## py, python
pythonのコードを実行します。  
### 使用例: 
```
!py
for i in range(5):
  print(i)
```
出力:
```
0
1
2
3
4
```

## js, javascript, node
JavaScript(node)のコードを実行します。
### 使用例: 
```
!js for(let i=0;i<5;i++) console.log(i);
```
出力:
```
0
1
2
3
4
```

## ts, typescript, ts-node
TypeScript(ts-node)のコードを実行します。
### 使用例: 
```
!ts for(let i=0;i<5;i++) console.log(i);
```
出力:
```
0
1
2
3
4
```

## cs, c#, csharp, csc
C#のコードを実行します
### 使用例: 
```
!cs class Program{static void Main(){
    for(int i=0;i<5;i++) System.Console.WriteLine(i); }}
```
出力:
```
0
1
2
3
4
```

## csi, csharpi, c#i
C# Scriptのコードを実行します。
### 使用例: 
```
!csi for(int i=0;i<5;i++) Print(i);
```
出力:
```
0
1
2
3
4
```