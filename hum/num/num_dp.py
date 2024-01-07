from functools import cache


class NumDp:
  def __init__(self, s_num):
    self.num = list(map(int, str(s_num)))
    self.n = len(self.num)

  def dp(self):
    return self.__dfs(0, 0, True, True)

  @cache
  def __dfs(self, i, st, limit, lead):
    if i == self.n:
      # 考虑能否取 0
      return 0 if lead else 1

    res = 0
    # 可以跳过当前数位
    if lead:
      res = self.__dfs(i + 1, st, False, True)

    up = self.num[i] if limit else 9
    # 根据前导0判断是否能取到0
    low = 1 if lead else 0

    for j in range(low, up + 1):
      # 处理某种条件
      if st >> j & 1 == 0:
        res += self.__dfs(i + 1, st | (1 << j), limit and j == up, False)

    return res
