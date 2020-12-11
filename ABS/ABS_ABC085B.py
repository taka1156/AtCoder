import test_case

_CASE = """\
7
50
30
50
100
50
80
30
"""

test_case.test_input(_CASE)

###########
# code
##########
n = int(input())
d = [int(input()) for i in range(n)]

d.sort(reverse=True)

tmp = d[0]
cnt = 1
for i in d:
    if tmp > i:
        tmp = i
        cnt += 1

print(cnt)
