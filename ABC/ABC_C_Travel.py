import test_case

_CASE = """\
5 5
0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0

"""

test_case.test_input(_CASE)

###########
# code
##########
import itertools

n, k = map(int, input().split())
t = []

ans = 0

for _ in range(n):
    s = list(map(int, input().split()))
    t.append(s)

for per in itertools.permutations(range(1, n)):
    score = 0
    prev = 0
    for i in range(n - 1):
        cur = per[i]
        score += t[prev][cur]
        prev = cur
    score += t[prev][0]

    if score == k:
        ans += 1

print(ans)
