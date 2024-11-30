names = ["tanaka", "yamada", "onishi"]

#passのパターン
for name in names:
    if name == "onishi":
        pass
    else:
        print(name)
    #onishiだったとき、
    #ifの処理だけが飛ぶので
    #ここのprintは実行される
    print("＊名前が選択されました")

#continueのパターン
for name in names:
    if name == "onishi":
        continue
    else:
        print(name)
    #onishiだったとき、
    #つぎのループに飛ぶので
    #ここのprintは実行されない
    print("＊名前が選択されました")