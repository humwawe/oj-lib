class FenwickTree:
  def __init__(self, n):
    self.N = n
    self.bit = [0] * n

  def set_bit(self, arr):
    self.bit = arr[:]

    for i in range(self.N):
      if i | (i + 1) < self.N:
        self.bit[i | (i + 1)] += self.bit[i]

  # [ ]
  def get_sum(self, l, r):
    return self.__get_sum(r) - self.__get_sum(l - 1)

  def __get_sum(self, r):
    res = 0
    while r >= 0:
      res += self.bit[r]
      r = (r & (r + 1)) - 1
    return res

  def add(self, idx, v):
    while idx < self.N:
      self.bit[idx] += v
      idx = idx | (idx + 1)

  def get(self, idx):
    return self.get_sum(idx, idx)

  def set(self, idx, v):
    self.add(idx, v - self.get(idx))
