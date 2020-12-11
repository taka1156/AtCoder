import test_case

_CASE = """\
100 4 16

"""

test_case.test_input(_CASE)

###########
# code
##########


def str_sum(c):
    total = 0
    tmp = str(c)
    for i in tmp:
        total += int(i)
    return total


n, a, b = map(int, input().split())

total = 0
for i in range(n + 1):
    tmp = str_sum(i)
    if tmp >= a and tmp <= b:
        total += i

print(total)
