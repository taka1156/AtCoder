import test_case

_CASE = """\
5
1000 1000 1000 1000 1000

"""

test_case.test_input(_CASE)

###########
# code
##########
N = int(input())
A = list(map(int, input().split()))

ans = -1
m = 0

for i in range(2, 1001):
    s = sum(a % i == 0 for a in A)
    if m < s:
        m = s
        ans = i

print(ans)
