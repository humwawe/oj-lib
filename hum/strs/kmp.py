"""
计算 s[0:] 和 s[i:] 之间的最长公共前缀（lcp）
z[0] = 0
"""


def z_function(s):
  n = len(s)
  z = [0] * n
  l, r = 0, 0
  for i in range(1, n):
    if i <= r and z[i - l] < r - i + 1:
      z[i] = z[i - l]
    else:
      z[i] = max(0, r - i + 1)
      while i + z[i] < n and s[z[i]] == s[i + z[i]]:
        z[i] += 1
    if i + z[i] - 1 > r:
      l = i
      r = i + z[i] - 1
  return z


"""
kmp[i] 为满足 s[0:z-1] = s[i-z:i-1] 的最大 z 值，
匹配不能都从0开始，否则z 等于 i 均为 s[0:i-1] = s[0:i-1]
kmp[0] = -1
  
  0  1  2  3  4  5  6
  a  a  b  a  a  b  # 
[-1, 0, 1, 0, 1, 2, 3]
"""


def kmp_pre(s):
  n = len(s)
  kmp = [0] * (n + 1)
  kmp[0] = -1
  j = 0
  for i in range(1, n):
    while j >= 0 and s[i] != s[j]:
      j = kmp[j]
    j += 1
    kmp[i + 1] = j
  return kmp

