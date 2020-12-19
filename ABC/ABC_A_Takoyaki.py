import test_case

_CASE = """\
1000 1 1000

"""

test_case.test_input(_CASE)

###########
# code
##########
import math

N, X, T = map(int, input().split())


print(math.ceil(N / X) * T)
