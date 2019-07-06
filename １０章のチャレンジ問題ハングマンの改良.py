import random

def hangman(word):# 引数wordはプレーヤー２に当てて欲しい単語
    wrong = 0  # 間違えた回数が加算される
    stages = ["",
              "___________       ",
              "|         |       ",
              "|         |       ",
              "|         O       ",
              "|       ／|＼     ",
              "|       ／ ＼     ",
              "|                 "
              ]
    rletters = list(word) # rletters はwordの文字を１文字ずつ分解してリストにしたもの
    board = ["_"] * len(word) # リスト変数boardはヒントの文字列を記録
    win = False   # winはプレイヤー２が勝利したらTrueになる
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1 :
        print("\n")
        msg = "１文字を予想してね"
        char = input(msg)

        if char in rletters : # １文字当てた場合
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
            
        else: # １文字が外れた場合
            wrong += 1

        print(" ".join(board)) # これまでに当てた文字だけ表示
        
        e = wrong + 1  # 間違った回数
        print("\n".join(stages[0:e])) # ハングマンの表示

        if "_" not in board :
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
        
    if not win :
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！　正解は {}.".format(word))


ans_list = ["cat", "dog", "bird", "deer", "fish", "hen", "frog", "pig"]
num_of_list = len(ans_list)
index_answer = random.randint(0, num_of_list)

hangman(ans_list[index_answer])
