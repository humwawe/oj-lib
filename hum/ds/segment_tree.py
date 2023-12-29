class SegmentTree:
  def __init__(self, n, op):
    self.N = n
    # op max -> -inf, min-> inf
    self.INF = float('inf')
    self.SIZE = 1 << (n - 1).bit_length()
    self.data = [0] * (2 * self.SIZE)
    self.OP = op

  def __push_up(self, k):
    self.data[k] = self.OP(self.data[2 * k], self.data[2 * k + 1])

  def build(self, arr):
    for i in range(self.N):
      self.data[self.SIZE + i] = arr[i]
    for i in range(self.SIZE - 1, 0, -1):
      self.__push_up(i)

  def modify(self, p, x):
    p += self.SIZE
    self.data[p] = x
    p >>= 1
    while p >= 1:
      self.__push_up(p)
      p >>= 1

  def get(self, p):
    return self.data[p + self.SIZE]

  def query(self, l, r):
    # [l,r)
    if l >= r:
      return self.INF
    sml = smr = self.INF
    l += self.SIZE
    r += self.SIZE
    while l < r:
      if l & 1:
        sml = self.OP(sml, self.data[l])
        l += 1
      if r & 1:
        r -= 1
        smr = self.OP(self.data[r], smr)
      l >>= 1
      r >>= 1
    return self.OP(sml, smr)

  def all_prod(self):
    return self.data[1]

  def search(self, l, r, x):
    l += self.SIZE
    r += self.SIZE
    l_min = -1
    r_min = -1
    while l < r:
      if l & 1:
        if self.OP(self.data[l], x) == self.data[l] and l_min == -1:
          l_min = l
        l += 1
      if r & 1:
        r -= 1
        if self.OP(self.data[r], x) == self.data[r]:
          r_min = r
      l >>= 1
      r >>= 1

    if l_min != -1:
      pos = l_min
      while pos < self.SIZE:
        if self.OP(self.data[2 * pos], x) == self.data[2 * pos]:
          pos = 2 * pos
        else:
          pos = 2 * pos + 1
      return pos - self.SIZE
    elif r_min != -1:
      pos = r_min
      while pos < self.SIZE:
        if self.OP(self.data[2 * pos], x) == self.data[2 * pos]:
          pos = 2 * pos
        else:
          pos = 2 * pos + 1
      return pos - self.SIZE
    else:
      return -1
