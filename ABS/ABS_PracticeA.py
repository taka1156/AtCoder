import test_case

_CASE = """\
72
128 256
myonmyon

"""

test_case.test_input(_CASE)

###########
# code
##########
a = int(input())
b, c = map(int, input().split())
s = input()

print(a + b + c, s)
