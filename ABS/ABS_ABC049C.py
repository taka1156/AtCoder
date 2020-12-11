# https://satoshi-blog.com/atcoder-beginners-selection-9
# わからなかったので調べた
import test_case

_CASE = """\
dreameraser
"""

test_case.test_input(_CASE)

###########
# code
##########
s = input()

s = s.replace("eraser", "")
s = s.replace("erase", "")
s = s.replace("dreamer", "")
s = s.replace("dream", "")

if s != "":
    print("NO")
else:
    print("YES")
