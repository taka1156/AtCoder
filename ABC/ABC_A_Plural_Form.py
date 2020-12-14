import test_case

_CASE = """\
box

"""

test_case.test_input(_CASE)

###########
# code
##########
s = input()

if s[len(s) - 1] == "s":
    s = s + "es"
else:
    s = s + "s"

print(s)
