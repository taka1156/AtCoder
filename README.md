# AtCoder練習用

- [Python入門（Python版 APG4b） - Qiita](./APG4b/README.md)
- [AtCoder Beginners Selection](./ABS/README.md)
- [AtCoder Problem](https://kenkoooo.com/atcoder#/table/taka1156)

## code
## 入力
- input, split
- map
- tuple

##　計算系
- abs
- +. -, *, /, %, //
- floor, ceil (切り下げ、切り上げ)
- 階乗
  ```python
  import math

  print(math.factorial(5))
  ```
- 順列
  ```python
  import itertools
  print(itertools.permutations(range(1, n)))
  ```

  ```python
  import math

  def f(n, r):
    return math.factorial(n) // math.factorial(n - r)

  print(f(6, 3))
  ```
- 組み合わせ
  ```python
  import math

  def f(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

  print(f(6, 3))
  ```
  
## 型変換
- int
- str
- float

# リスト
- list
- all, any
- sort
- sorted
- sum
- len
- set
- min, max

# その他

