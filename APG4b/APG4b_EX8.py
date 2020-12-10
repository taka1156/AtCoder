# https://atcoder.jp/contests/apg4b/tasks/APG4b_co
"""
p = int(input())  # パターン

# パターン1
if p == 1:
    price = int(input())  # 価格
    n = int(input())  # 個数
    print(price * n)  # 値段

# パターン2
if p == 2:
    text = input()
    price = int(input())  # 価格
    n = int(input())  # 個数
    print(text + "!")  # 説明
    print(price * n)  # 値段
"""

# ==修正==
p = int(input())  # パターン

# パターン2
if p == 2:
    text = input()
    print(text + "!")  # 説明

price = int(input())  # 価格
n = int(input())  # 個数
print(price * n)  # 値段
