import test_case

_CASE = """\
30
40
50
6000

"""

test_case.test_input(_CASE)

###########
# code
##########
a = int(input()) + 1
b = int(input()) + 1
c = int(input()) + 1
x = int(input())

cnt = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            if x == 500 * i + 100 * j + 50 * k:
                cnt += 1

print(cnt)
