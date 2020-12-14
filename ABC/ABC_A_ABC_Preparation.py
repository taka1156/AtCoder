import test_case

_CASE = """\
100 100 1 100

"""

test_case.test_input(_CASE)

###########
# code
##########
a = list(map(int, input().split()))

ans = a[0]
for n in a:
    if n < ans:
        ans = n

print(ans)
