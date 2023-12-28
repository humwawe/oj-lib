class SegmentTree:
  def __init__(self, n, op):
    self.n = n
    self.inf = float('inf')
    self.log = (n - 1).bit_length()
    self.size = 1 << self.log
    self.data = [0] * (2 * self.size)
    self.op = op

  def __push_up(self, k):
    self.data[k] = self.op(self.data[2 * k], self.data[2 * k + 1])

  def build(self, arr):
    for i in range(self.n):
      self.data[self.size + i] = arr[i]
    for i in range(self.size - 1, 0, -1):
      self.__push_up(i)

  def modify(self, p, x):
    p += self.size
    self.data[p] = x
    p >>= 1
    while p >= 1:
      self.__push_up(p)
      p >>= 1

  def get(self, p):
    return self.data[p + self.size]

  def query(self, l, r):
    # [l,r)
    if l >= r:
      return self.inf
    sml = smr = self.inf
    l += self.size
    r += self.size
    while l < r:
      if l & 1:
        sml = self.op(sml, self.data[l])
        l += 1
      if r & 1:
        r -= 1
        smr = self.op(self.data[r], smr)
      l >>= 1
      r >>= 1
    return self.op(sml, smr)

  def all_prod(self):
    return self.data[1]

  def search(self, l, r, x):
    l += self.size
    r += self.size
    l_min = -1
    r_min = -1
    while l < r:
      if l & 1:
        if self.op(self.data[l], x) == self.data[l] and l_min == -1:
          l_min = l
        l += 1
      if r & 1:
        r -= 1
        if self.op(self.data[r], x) == self.data[r]:
          r_min = r
      l >>= 1
      r >>= 1

    if l_min != -1:
      pos = l_min
      while pos < self.size:
        if self.op(self.data[2 * pos], x) == self.data[2 * pos]:
          pos = 2 * pos
        else:
          pos = 2 * pos + 1
      return pos - self.size
    elif r_min != -1:
      pos = r_min
      while pos < self.size:
        if self.op(self.data[2 * pos], x) == self.data[2 * pos]:
          pos = 2 * pos
        else:
          pos = 2 * pos + 1
      return pos - self.size
    else:
      return -1
