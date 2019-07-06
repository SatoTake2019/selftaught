# 第４章のチャレンジ問題（p.69）
#１～６までの問題をいっぺんにこのプログラムに書きます。

#１ 数字を入力値として受け取り、その数字を２乗した戻り値を返す関数を書いてみよう。

def square():
    """
    戻り値：入力した値の二乗（int）
    """
    x = int(input("数字を入力してください："))

    return x * x

#２ 文字列を引数とし、その文字列を出力する関数を書いてみよう。

def print_strings( c ):
    """
    str c 文字列の引数
    引数を標準出力に印字する関数
    return: none
    """
    print(c)

#３ ３つの必須引数と２つのオプション引数がある関数を書いてみよう。
    
def print_profile(name, sex, age, country="日本", tel_no="09000000000"):
    print("氏名")
    print(name)
    print("年齢")
    print(age)
    print("国籍")
    print(country)
    print("電話番号")
    print(tel_no)



#４ ２つの関数からなるプログラムを書いてみよう。
#   １つ目の関数は整数を引数として受け取り、
#   その整数を２で割って求められる整数を出力として返そう。
#   ２つ目の関数は、整数を引数として受け取り、４を掛けた整数を返そう。
#   プログラム内で、１つ目の関数を呼び、戻り値を変数として保存し、
#   ２つ目の関数の引数として渡そう。
def devide(x):
    """
    int x
    return x // 2
    """
    return x // 2

def by_four(x):
    """
    int x
    return x * 4
    """
    return x * 4

y = devide(9)
by_four(y)

#５  文字列を float 型に変換して戻り値とする関数を書いてみよう。
#    起こりうる例外をキャッチする例外処理を書こう。
def str_to_float(string):
    """
    str string
    return float number
    """
    try:
        return float(string)
    
    except(ValueError, NameError):
        print("不正な引数です。")


#６　（一部割愛）めんどい


# 解答例　　http://tinyurl.com/hkzgqrv







