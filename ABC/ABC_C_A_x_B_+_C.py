import test_case

_CASE = """\
1000000

"""

test_case.test_input(_CASE)

###########
# code
##########
n = int(input())

cnt = 0
for i in range(1, n):
    cnt += (n - 1) // i
print(cnt)
