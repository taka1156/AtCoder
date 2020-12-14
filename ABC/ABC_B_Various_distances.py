from decimal import Decimal
import test_case

_CASE = """\
10
3 -1 -4 1 -5 9 2 -6 5 -3

"""

test_case.test_input(_CASE)

###########
# code
##########
n = int(input())
x = list(map(int, input().split()))

m, u, c = 0, 0, 0

for i in x:
    m += abs(i)
    u += i ** 2
    c = max(c, abs(i))

re1 = u ** 0.5

print(m)
print(re1)
print(c)
