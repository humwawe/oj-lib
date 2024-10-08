def dfs(tree, u):
  n = len(tree)
  dis = [0] * n
  cur_path = []

  p = [-1] * n

  stack = [u]
  dfs_order = []
  while stack:
    u = stack.pop()
    if u >= 0:
      cur_path.append(u)
      dfs_order.append(u)
      stack.append(~u)
      for v, w in tree[u]:
        if v == p[u]:
          continue
        p[v] = u
        stack.append(v)
        dis[v] = dis[u] + w

    else:
      cur_path.pop()

  return dfs_order
