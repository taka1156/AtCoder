import test_case

_CASE = """\
6
1 1
2 2
3 3
4 4
5 5
6 6

"""

test_case.test_input(_CASE)

###########
# code
##########
n = int(input())

cnt = 0
ans = "No"
for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        cnt += 1
        if cnt == 3:
            ans = "Yes"
            break
    else:
        cnt = 0

print(ans)
