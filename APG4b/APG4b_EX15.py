import test_case

_CASE = """\
2
5 7
4 10
9 2
"""

test_case.test_input(_CASE)

###########
# code
##########
"""
1人のテストの点数を表すリストから合計点を計算して返す関数
引数 scores: scores[i]にi番目のテストの点数が入っている
返り値: 1人のテストの合計点
"""


def sum_scores(scores):
    return sum(scores)
    # ここにプログラムを追記


"""
3人の合計点からプレゼントの予算を計算して出力する関数
引数 sum_a: A君のテストの合計点
引数 sum_b: B君のテストの合計点
引数 sum_c: C君のテストの合計点
返り値: なし
"""


def output(sum_a, sum_b, sum_c):
    # ここにプログラムを追記
    print(sum_a * sum_b * sum_c)


# ---------------------
# ここから先は変更しない
# ---------------------

# 1行の整数が空白区切りになった入力を受け取ってリストに入れて返す関数
# 引数 s: 1行の、整数が空白区切りになった入力
# 返り値: 受け取った入力のリスト
def list_int_input(s):
    a = list(map(int, s.split()))
    return a


# 科目数Nを受け取る
n = int(input())

# それぞれのテストの点数を受け取る
a = list_int_input(input())
b = list_int_input(input())
c = list_int_input(input())

# プレゼントの予算を出力
output(sum_scores(a), sum_scores(b), sum_scores(c))
