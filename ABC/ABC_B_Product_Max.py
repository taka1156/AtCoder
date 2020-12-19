import test_case

_CASE = """\
-1000000000 0 -1000000000 0

"""

test_case.test_input(_CASE)

###########
# code
##########
a, b, c, d = map(int, input().split())

print(max(max(a * c, a * d), max(b * c, b * d)))

# 最大になるパターンは
# 範囲がプラス側のみの場合、`-x * -y, x * y`
# 範囲がマイナス側のみの場合は` -x * x, x * -y`
