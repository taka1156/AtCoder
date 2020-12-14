import test_case

_CASE = """\
100 100
100 100

"""

test_case.test_input(_CASE)

###########
# code
##########
a, b = map(int, input().split())
c, d = map(int, input().split())

print(a * d - b * c)
