class Factorial:
  def __init__(self, n, mod) -> None:
    n += 5
    self.mod = mod
    self.f = [1 for _ in range(n)]
    self.g = [1 for _ in range(n)]

    for i in range(1, n):
      self.f[i] = self.f[i - 1] * i % self.mod

    # self.g[-1] = pow(self.f[-1], mod - 2, mod)
    self.g[-1] = pow(self.f[-1], -1, mod)

    for i in range(n - 2, -1, -1):
      self.g[i] = self.g[i + 1] * (i + 1) % self.mod

  def fac(self, n):
    return self.f[n]

  def fac_inv(self, n):
    return self.g[n]

  def comb(self, n, m):
    if n < m or m < 0 or n < 0: return 0
    return self.f[n] * self.g[m] % self.mod * self.g[n - m] % self.mod

  def perm(self, n, m):
    if n < m or m < 0 or n < 0: return 0
    return self.f[n] * self.g[n - m] % self.mod

  def catalan(self, n):
    return (self.comb(2 * n, n) - self.comb(2 * n, n - 1)) % self.mod

  def inv(self, n):
    return self.f[n - 1] * self.g[n] % self.mod

