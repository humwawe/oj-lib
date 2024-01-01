from typing import List, Tuple


def get_biconnected_components(G: List[List[int]]) -> Tuple[List[List[int]], List[List[Tuple[int, int]]]]:
  n = len(G)
  order = [-1] * n
  lowlink = [-1] * n
  indx = [0] * n
  par = [-1] * n

  cur_time = 0
  stack = []

  vertex_ans = []

  def dfs(v: int) -> None:
    nonlocal cur_time
    par[v] = -2
    while v >= 0:
      if indx[v] == len(G[v]):
        p = par[v]
        if p < 0:
          break
        lowlink[p] = min(lowlink[p], lowlink[v])
        if lowlink[v] >= order[p]:
          min_vx, max_vx = min(v, p), max(v, p)
          this_vertex_ans = []
          while True:
            a, b = stack.pop()
            this_vertex_ans.append(a)
            this_vertex_ans.append(b)
            if min_vx == a and max_vx == b:
              break
          vertex_ans.append(list(set(this_vertex_ans)))
        v = p
        continue

      x = G[v][indx[v]]
      indx[v] += 1
      if indx[v] == 1:
        order[v] = cur_time
        lowlink[v] = cur_time
        cur_time += 1
      if x != par[v] and order[x] < order[v]:
        stack.append((min(v, x), max(v, x)))
      if par[x] != -1:
        if order[x] != -1:
          lowlink[v] = min(lowlink[v], order[x])
        continue
      v, par[x] = x, v

  for root in range(n):
    if order[root] == -1:
      pre_len = len(vertex_ans)
      dfs(root)
      if len(vertex_ans) == pre_len:
        vertex_ans.append([root])
  return vertex_ans
