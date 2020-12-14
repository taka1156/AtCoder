import test_case

_CASE = """\
-9 99 -999 9999

"""

test_case.test_input(_CASE)

###########
# code
##########
sx, sy, gx, gy = map(int, input().split())

# ans = float((sx * gy + gx * sy) / (sy + gy))
ans = float((gx - sx) * sy / (sy + gy) + sx)

print(ans)
