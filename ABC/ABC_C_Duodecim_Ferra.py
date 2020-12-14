import test_case
import math

_CASE = """\
17

"""

test_case.test_input(_CASE)

###########
# code
##########


def f(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


n = int(input())

ans = f(n - 1, 11)

print(ans)
