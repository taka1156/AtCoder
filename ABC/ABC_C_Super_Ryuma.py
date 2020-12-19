import test_case

_CASE = """\
1 1
5 6

"""

test_case.test_input(_CASE)

###########
# code
##########
a, b = map(int, input().split())
c, d = map(int, input().split())

c -= a
d -= b

x = abs(c)
y = abs(d)

ans = 0

if x == y == 0:  # 移動なし
    ans = 0
elif x == y or x + y <= 3:  # 斜め移動もしくは、上下左右三回移動でいける
    ans = 1
elif x % 2 == y % 2 or x + y <= 6 or abs(x - y) <= 3:  # 斜め移動、 上下左右三回移動を二回でいける
    ans = 2
else:  # それ以外
    ans = 3

print(ans)
