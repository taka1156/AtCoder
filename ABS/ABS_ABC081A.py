import test_case

_CASE = """\
101

"""

test_case.test_input(_CASE)

###########
# code
##########
s = input()

cnt = 0
for b in s:
    if b == "1":
        cnt += 1

print(cnt)
