import test_case

_CASE = """\
10 3

"""

test_case.test_input(_CASE)

###########
# code
##########
N, W = map(int, input().split())

print(int(N / W))
