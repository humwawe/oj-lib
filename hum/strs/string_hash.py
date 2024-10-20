import random


class StringHash:
  def __init__(self, s):
    self.N = len(s)
    self.BASE = 131  # random.randint(100, 500)
    self.MOD = random.getrandbits(64)
    self.h = h = [0] * (self.N + 1)
    self.p = p = [1] * (self.N + 1)
    for i in range(1, self.N + 1):
      p[i] = (p[i - 1] * self.BASE) % self.MOD
      h[i] = (h[i - 1] * self.BASE + ord(s[i - 1])) % self.MOD

  # [l,r)
  def __get_hash(self, l, r):
    return (self.h[r] - self.h[l] * self.p[r - l]) % self.MOD

  def __getitem__(self, item) -> int:
    if isinstance(item, int):
      return (self.h[item + 1] - self.h[item] * self.p[1]) % self.MOD
    else:
      l, r = item.start, item.stop
      if l is None:
        l = 0
      if r is None:
        r = self.N
      return self.__get_hash(l, r)
