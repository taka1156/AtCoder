import test_case

_CASE = """\
0

"""

test_case.test_input(_CASE)

###########
# code
##########
if int(input()) == 0:
    print("1")
else:
    print("0")
