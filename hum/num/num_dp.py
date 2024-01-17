from functools import cache


def dp(s_num):
  num = list(map(int, str(s_num)))
  n = len(num)

  @cache
  def __dfs(i, st, limit, lead):
    if i == n:
      # 考虑能否取 0
      return 0 if lead else 1

    res = 0
    # 可以跳过当前数位
    if lead:
      res = __dfs(i + 1, st, False, True)

    up = num[i] if limit else 9
    # 根据前导0判断是否能取到0
    low = 1 if lead else 0

    for j in range(low, up + 1):
      # 处理某种条件
      if st >> j & 1 == 0:
        res += __dfs(i + 1, st | (1 << j), limit and j == up, False)

    return res

  return __dfs(0, 0, True, True)
