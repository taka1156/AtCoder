# https://atcoder.jp/contests/apg4b/tasks/APG4b_cm
def graph(p, n):
    print("{0}:".format(p), end="")
    i = 0
    while i < n:
        print("]", end="")
        i += 1
    print()


a, b = map(int, input().split())

graph("A", a)

graph("B", b)
