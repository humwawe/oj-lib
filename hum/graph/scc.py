def find_SCC(graph, n):
  SCC = []
  S, P = [], []
  depth = [0] * n

  stack = list(range(n))
  while stack:
    node = stack.pop()
    if node < 0:
      d = depth[~node] - 1
      if P[-1] > d:
        SCC.append(S[d:])
        del S[d:], P[-1]
        for node in SCC[-1]:
          depth[node] = -1
    elif depth[node] > 0:
      while P[-1] > depth[node]:
        P.pop()
    elif depth[node] == 0:
      S.append(node)
      P.append(len(S))
      depth[node] = len(S)
      stack.append(~node)
      stack.extend(graph[node])
  return SCC[::-1]
  # new_n = len(SCC)


def find_SCC(graph, n):
  col = [-1] * n
  S, P = [], []
  cur = 0

  depth = [0] * n

  stack = list(range(n))
  while stack:
    node = stack.pop()
    if node < 0:
      d = depth[~node] - 1
      if P[-1] > d:
        P.pop()
        while len(S) > d:
          u = S.pop()
          col[u] = cur
          depth[u] = -1
        cur += 1
    elif depth[node] > 0:
      while P[-1] > depth[node]:
        P.pop()
    elif depth[node] == 0:
      S.append(node)
      P.append(len(S))
      depth[node] = len(S)
      stack.append(~node)
      stack.extend(graph[node])
  return col
  # new_n = max(col) + 1
