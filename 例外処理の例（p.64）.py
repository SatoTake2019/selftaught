# 例外処理の例

a = input("Type a number :")
b = input("Type another  :")
a = int(a)
b = int(b)

try:
    print(a / b)
except ZeroDivisionError:
    print("b cannot be zero.")

print("このプログラムの末尾まで来ました。")


