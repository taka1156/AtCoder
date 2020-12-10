# https://atcoder.jp/contests/apg4b/tasks/APG4b_cr
"""
a, op, b = input().split(" ")

a = int(a)
b = int(b)

result = ""

if op == "+":
    result = str(a + b)
elif op == "-":
    result = str(a - b)
elif op == "*":
    result = str(a * b)
elif op == "/" and b != 0:
    result = str(a // b)  # 小数点の場合は、切り捨てて出力
else:
    result = "error"

print(result)
"""

# 問題をよく読む => (小数点の場合は、切り捨てて出力)
# 結果を、一々変数に入れずにそのままprintしたほうがいい？
# 変な空白が混らないようにeditorを使う
# 負数が入るときは`a//b`使えない?
# => 代替案? [decimal](https://docs.python.org/ja/3/library/decimal.html)

# ==修正==

a, op, b = input().split(" ")

a = int(a)
b = int(b)

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/" and b != 0:
    print(a // b)  # 小数点の場合は、切り捨てて出力
else:
    print("error")
