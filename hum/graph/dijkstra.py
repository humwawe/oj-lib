from heapq import heappop, heappush
from math import inf


def dijkstra(graph, src):
  n = len(graph)
  dist = [inf] * n
  vis = [False] * n
  hpq = [(0, src)]
  dist[src] = 0

  while hpq:
    d, u = heappop(hpq)
    if vis[u]:
      continue
    vis[u] = True

    for v, w in graph[u]:
      if dist[v] > d + w:
        dist[v] = d + w
        heappush(hpq, (dist[v], v))

  return dist
