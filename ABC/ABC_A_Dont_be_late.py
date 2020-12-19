import test_case

_CASE = """\
10000 1 1


"""

test_case.test_input(_CASE)

###########
# code
##########
D, T, S = map(int, input().split())

if D / S <= T:
    print("Yes")
else:
    print("No")
