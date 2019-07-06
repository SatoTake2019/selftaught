answer = input("好きな色は何ですか？")

with open("d:\\My Document Files\\WEBシステム\\独学プログラマ\\fav_color.txt", "w", encoding="utf-8") as f:
    f.write(answer)

