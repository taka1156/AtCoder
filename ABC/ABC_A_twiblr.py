import test_case

_CASE = """\
10000 0

"""

test_case.test_input(_CASE)

###########
# code
##########
a, b = map(int, input().split())

print((2 * a) + 100 - b)
