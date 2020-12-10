import test_case

_CASE1 = """\
3 2
1 2
3 1
"""

_CASE2 = """\
7 12
1 5
5 4
6 2
1 7
2 4
6 3
1 3
6 4
3 7
5 7
4 3
6 1
"""

_CASE3 = """\
1 0
"""

# ヒント
_CASE4 = """\
4 6
1 2
1 3
1 4
2 3
2 4
3 4
"""

_CASE5 = """\
20 56
14 18
8 19
18 20
5 15
17 3
12 15
7 3
14 12
18 17
2 12
4 12
17 5
11 10
14 13
8 5
8 1
16 13
17 7
16 18
20 8
10 7
9 20
17 11
8 2
6 4
9 19
13 3
7 15
13 9
4 2
18 7
20 2
17 2
8 18
5 16
1 12
6 1
11 2
9 6
11 15
17 19
18 6
8 17
15 10
10 6
1 18
15 19
9 7
2 14
4 19
20 11
16 12
5 2
16 9
13 2
12 20
"""

test_case.test_input(_CASE1)

###########
# code
##########

n, m = map(int, input().split())

# t = [["-"] * n] * n
t = [["-" for i in range(n)] for j in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    t[x - 1][y - 1] = "o"
    t[y - 1][x - 1] = "x"

for i in range(n):
    for j in range(n):
        print(t[i][j], end="")
        if j < n - 1:
            print(" ", end="")
    print()
