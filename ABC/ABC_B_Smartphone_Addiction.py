import test_case

_CASE = """\
10 2 20
9 11
13 17

"""

test_case.test_input(_CASE)

###########
# code
##########
n, m, t = map(int, input().split())

tmp = 0
battery = n
for i in range(m):
    a, b = map(int, input().split())
    battery = max(0, battery - (a - tmp))
    tmp = b
    if battery == 0:
        break
    battery = min(n, battery + (b - a))

if battery != 0:
    battery = max(0, battery - (t - tmp))

if battery == 0:
    print("No")
else:
    print("Yes")
