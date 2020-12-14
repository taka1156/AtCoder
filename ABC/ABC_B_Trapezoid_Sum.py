import test_case

_CASE = """\
1
1 1000000

"""

test_case.test_input(_CASE)

###########
# code
##########
n = int(input())

# 等差数列の和
total = 0
for _ in range(n):
    a, b = map(int, input().split())
    c = b - a + 1
    total += (a + b) * c // 2

print(total)
