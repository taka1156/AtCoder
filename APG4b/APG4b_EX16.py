import test_case

_CASE = """\
5 3 3 1 4

"""

test_case.test_input(_CASE)

###########
# code
##########
"""
ループを使わないで書く
パターンを見つける
ループで書き直す
"""
a = list(map(int, input().split()))

# ループを使わない
"""
result = "NO"
# 回数は0~4
if a[0] == a[1]:
    result = "YES"

if a[1] == a[2]:
    result = "YES"

if a[2] == a[3]:
    result = "YES"

if a[3] == a[4]:
    result = "YES"
"""

# ループを使う
result = "NO"
for i in range(4):
    if a[i] == a[i + 1]:
        result = "YES"

print(result)
