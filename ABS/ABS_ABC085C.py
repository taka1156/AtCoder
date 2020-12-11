import test_case

_CASE = """\
2000 20000000

"""

test_case.test_input(_CASE)

###########
# code
##########
n, y = map(int, input().split())
# a + b + c = 9
# 10000a + 5000b + 1000c = 45000

result = "-1 -1 -1"

for a in range(n + 1):
    for b in range(n + 1 - a):
        c = n - (a + b)
        if 10000 * a + 5000 * b + 1000 * c == y:
            result = str(a) + " " + str(b) + " " + str(c)

print(result)
