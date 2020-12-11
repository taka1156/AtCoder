import test_case

_CASE = """\
2
3 1 2
6 1 1

"""

test_case.test_input(_CASE)

###########
# code
##########
n = int(input())
t0, x0, y0 = 0, 0, 0
cnt = 0

for i in range(n):
    t, x, y = map(int, input().split())
    distance = abs(x - x0) + abs(y - y0)
    time = abs(t - t0)
    t0 = t
    x0 = x
    y0 = y

    if distance > time or distance % 2 != time % 2:
        cnt += 1
    else:
        cnt = 0

if cnt == 0:
    print("Yes")
else:
    print("No")
