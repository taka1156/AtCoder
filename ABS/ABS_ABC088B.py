import test_case

_CASE = """\
4
20 18 2 18

"""

test_case.test_input(_CASE)

###########
# code
##########
n = int(input())
a = list(map(int, input().split()))

alice, bob = 0, 0

a.sort(reverse=True)

alice = sum([a[i] for i in range(0, n, 2)])
bob = sum([a[i] for i in range(1, n, 2)])

print(alice - bob)
