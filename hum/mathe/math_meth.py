def primes(n):  # 埃氏筛法，从x ^ 2 开始，将x ^ 2, (x + 1) * x,..n / x * x标记
  pr = [] * (n + 1)
  vis = [False] * (n + 1)
  for i in range(2, n + 1):
    if vis[i]: continue
    pr.append(i)
    for j in range(i * i, n + 1, i):
      vis[j] = True


def primes_sieve(n):  # 线性筛，被最小质因子筛掉
  pr = [] * (n + 1)
  vis = [False] * (n + 1)
  for i in range(2, n + 1):
    if not vis[i]:
      pr.append(i)
    for p in pr:
      if (t := p * i) > n:
        break
      vis[t] = True
      if i % p == 0:
        break


def primes_lpf(n):  # lpf[i] 记录每个数最小的质因子
  pr = [] * (n + 1)
  lpf = [0] * (n + 1)
  for i in range(2, n + 1):
    if lpf[i] == 0:
      lpf[i] = i
      pr.append(i)
    for p in pr:
      if (t := p * i) > n or p > lpf[i]:
        break
      lpf[t] = p


# 欧拉函数: n 以内与 n 互质的个数
# N = p1 ^ c1 * p2 ^ c2 * ... * pk ^ ck
# euler(n) = N * (1 - 1 / p1) * (1 - 1 / p2) * ... * (1 - 1 / pk)
def eulers(n):
  vis = [False] * (n + 1)
  e = [0] * (n + 1)
  pr = []
  for i in range(2, n + 1):
    if not vis[i]:
      pr.append(i)
      e[i] = i - 1
    for p in pr:
      if (t := p * i) > n:
        break
      vis[t] = True
      if i % p == 0:
        e[t] = e[i] * p
        break
      e[t] = e[i] * (p - 1)
