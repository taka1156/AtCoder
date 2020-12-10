# 変数a, b, cにTrueまたはFalseを代入してAtCoderと出力されるようにする
a = True
b = False
c = True

# ここから先は変更しないこと

if a:
    print("At", end="")  # end="" と書くと末尾改行がされなくなる
else:
    print("Yo", end="")

if (not a) and b:
    print("Bo", end="")
elif (not b) and c:
    print("Co", end="")

if a and b and c:
    print("foo!")
elif True and False:
    print("yeah!")
elif (not a) or c:  # or
    print("der")
