import test_case

_CASE = """\
1 0
100
200
"""

test_case.test_input(_CASE)

# リンゴ・パイナップルをそれぞれ1つずつ選んで購入しようとする

###########
# code
##########
n, s = map(int, input().split())
a = list(map(int, input().split()))
p = list(map(int, input().split()))

cnt = 0
tmp = 0

"""
if a[0] + p[0] == s:
    cnt += 1

if a[0] + p[1] == s:
    cnt += 1

if a[0] + p[2] == s:
    cnt += 1
#############
if a[1] + p[0] == s:
    cnt += 1

if a[1] + p[1] == s:
    cnt += 1

if a[1] + p[2] == s:
    cnt += 1
#############

if a[2] + p[0] == s:
    cnt += 1

if a[2] + p[1] == s:
    cnt += 1

if a[2] + p[2] == s:
    cnt += 1
#############
"""

for i in range(n):
    for j in range(n):
        if a[i] + p[j] == s:
            cnt += 1

print(cnt)
