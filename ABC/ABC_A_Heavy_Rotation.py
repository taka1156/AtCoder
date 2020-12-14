import test_case

_CASE = """\
5

"""

test_case.test_input(_CASE)

###########
# code
##########
n = int(input())

if n % 2 == 0:
    print("White")
else:
    print("Black")
