class Matrix:

  def __init__(self, n, m):
    self.n = n
    self.m = m
    self.mat = [0] * (n * m)

  def init_matrix(self, a):
    # a 为二维数组
    self.n, self.m = len(a), len(a[0])
    self.mat = [0] * (self.n * self.m)
    for i in range(self.n):
      for j in range(self.m):
        self.mat[i * self.m + j] = a[i][j]


def matrix_mul(A, B, mod=10 ** 9 + 7):
  n, m = len(A), len(A[0])
  p = len(B[0])
  ans = [[0] * p for _ in range(n)]
  for i in range(n):
    for j in range(m):
      for k in range(p):
        ans[i][k] += A[i][j] * B[j][k]
        ans[i][k] %= mod
  return ans


def matrix_pow(x, n):
  if n == 0:
    k = len(x)
    grid = [[0] * k for _ in range(k)]
    for i in range(k):
      grid[i][i] = 1
    return grid
  if n == 1: return x
  if n == 2: return matrix_mul(x, x)
  v = matrix_pow(x, n // 2)
  ans = matrix_mul(v, v)
  if n % 2 == 0:
    return ans
  return matrix_mul(ans, x)
