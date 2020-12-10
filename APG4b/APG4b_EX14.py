import test_case

_CASE = """\
150 190 160
"""

test_case.test_input(_CASE)

###########
# code
##########
h = list(map(int, input().split()))

h.sort()

print(h[2] - h[0])
