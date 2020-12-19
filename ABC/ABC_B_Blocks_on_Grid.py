import test_case

_CASE = """\
2 3
2 2 3
3 2 2

"""

test_case.test_input(_CASE)

###########
# code
##########
import itertools

H, W = map(int, input().split())
a = [input().split() for l in range(H)]

for i in range(len(a)):
    a[i] = [int(j) for j in a[i]]

num = min(list(itertools.chain.from_iterable(a)))
cnt = 0

for i in range(H):
    for j in range(W):
        if a[i][j] > num:
            cnt += a[i][j] - num

print(cnt)
