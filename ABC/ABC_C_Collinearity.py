import test_case

_CASE = """\
14
5 5
0 1
2 5
8 0
2 1
0 0
3 6
8 6
5 9
7 9
3 4
9 2
9 8
7 2

"""

test_case.test_input(_CASE)

###########
# code
##########
n = int(input())
points = [tuple(map(int, input().split())) for i in range(n)]

ans = "No"
for i in range(n):
    for j in range(i):
        for k in range(j):
            x0, y0 = points[i]
            x1, y1 = points[j]
            x2, y2 = points[k]

            x0 -= x2
            x1 -= x2
            y0 -= y2
            y1 -= y2
            if x0 * y1 == x1 * y0:
                ans = "Yes"
                break

print(ans)
