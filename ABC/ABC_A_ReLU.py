import test_case

_CASE = """\
-1

"""

test_case.test_input(_CASE)

###########
# code
##########
x = int(input())

if x >= 0:
    print(x)

if x < 0:
    print(0)
