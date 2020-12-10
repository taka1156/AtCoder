# https://atcoder.jp/contests/apg4b/tasks/APG4b_cn
x, a, b = map(int, input().split())

x += 1
print(x)
x *= a + b
print(x)
x *= x
print(x)
x -= 1
print(x)

# ** より *　の方がはやい？
