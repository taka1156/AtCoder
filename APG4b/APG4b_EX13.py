import test_case

_CASE1 = """\
3
2 1 4
"""

_CASE2 = """\
2
80 70
"""

_CASE3 = """\
5
100 100 100 100 100
"""

_CASE4 = """\
10
53 21 99 83 75 40 33 62 18 100
"""

test_case.test_input(_CASE4)

###########
# code
##########

n = int(input())
a = list(map(int, input().split()))

ave = int(sum(a) / n)
for i in a:
    print(abs(i - ave))
