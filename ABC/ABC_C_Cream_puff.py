import test_case

_CASE = """\
519437318400

"""

test_case.test_input(_CASE)

###########
# code
##########
n = int(input())
result = set()

i = 1
while i * i <= n:
    if n % i == 0:
        result.add(i)
        result.add(n // i)

    i += 1

ans = list(result)
ans.sort()

for n in ans:
    print(n)

"""
i == n/1の時重複するので set(）を使い、list変換後にsortする
"""
