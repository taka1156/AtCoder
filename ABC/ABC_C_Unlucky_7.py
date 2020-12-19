import test_case

_CASE = """\
20

"""

test_case.test_input(_CASE)

###########
# code
##########
N = int(input())

cnt = 0
for i in range(1, N + 1):
    dec_s = str(i)
    oct_s = str(oct(i))

    if dec_s.find("7") == oct_s.find("7") == -1:
        cnt += 1

print(cnt)
