# https://atcoder.jp/contests/apg4b/tasks/APG4b_cl
"""
n = int(input())
a = int(input())

for i in range(1, n + 1):
    op, b = input().split()
    b = int(b)
    if op == "+":
        a += b
        print("{0}:{1}".format(i, a))
    elif op == "-":
        a -= b
        print("{0}:{1}".format(i, a))
    elif op == "*":
        a *= b
        print("{0}:{1}".format(i, a))
    elif op == "/" and b != 0:
        a //= b
        print("{0}:{1}".format(i, a))
    else:
        print("error")
        break
"""

# a//b　より int(a/b)した方がいい？
# => 代替案? [decimal](https://docs.python.org/ja/3/library/decimal.html)

import test_case

_CASE1 = """\
3
2
+ 1
* 3
/ 2
"""

_CASE2 = """\
2
3
/ 2
/ 2
"""

_CASE3 = """\
4
3
+ 1
/ 0
* 2
- 10
"""

_CASE4 = """\
7
10
* 10
* 10
* 10
* 10
* 10
* 10
* 10
"""

test_case.test_input(_CASE4)

###########
# code
##########

# ==修正==
n = int(input())
a = int(input())

for i in range(1, n + 1):
    op, b = input().split()
    b = int(b)
    if op == "+":
        a += b
    elif op == "-":
        a -= b
    elif op == "*":
        a *= b
    elif op == "/" and b != 0:
        a = int(a / b)
    else:
        print("error")
        break

    print("{0}:{1}".format(i, a))
