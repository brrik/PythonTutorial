names = ["tanaka", "yamada", "onishi"]

#passのパターン
for name in names:
    if name == "onishi":
        pass
    print("＊名前が選択されました")

#continueのパターン
for name in names:
    if name == "onishi":
        continue
    print("＊名前が選択されました")