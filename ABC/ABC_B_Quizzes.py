import test_case

_CASE = """\
20 10
xxxxxxxxxxxxxxxxxxxx

"""

test_case.test_input(_CASE)

###########
# code
##########
n, x = map(int, input().split())
s = input()

score = x
for i in s:
    if i == "x":
        score = max(0, score - 1)
    else:
        score += 1

print(score)
