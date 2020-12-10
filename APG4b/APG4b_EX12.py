import test_case

_CASE1 = """\
1+1+1-1
"""

_CASE2 = """\
1-1-1-1-1-1
"""

test_case.test_input(_CASE2)

###########
# code
##########

s = input()

total = 1

for c in s:
    tmp = 0
    if c == "+":
        total += 1
    if c == "-":
        total -= 1

print(total)
