# 例外処理の例 その２

#try: try は下の位置でも良いようです
a = input("Type a number :")
b = input("Type another  :")
try:
    a = int(a)
    b = int(b)
    print(a / b)
except(ZeroDivisionError, ValueError):
    print("Invalid input.")

print("このプログラムの末尾まで来ました。")


