import test_case

_CASE = """\
6
382253568 723152896 37802240 379425024 404894720 471526144
"""

test_case.test_input(_CASE)

###########
# code
##########
n = int(input())
a = list(map(int, input().split()))

cnt = 0
while all([i % 2 == 0 for i in a]):
    a = [i / 2 for i in a]
    cnt += 1

print(cnt)
