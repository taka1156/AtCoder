import test_case

_CASE = """\
100 1 1


"""

test_case.test_input(_CASE)

###########
# code
##########
n, a, b = map(int, input().split())

print(n - a + b)
