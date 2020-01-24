#Uses python3

import sys
from collections import defaultdict
from heapq import heappop, heappush

def distance(adj, cost, s, t):
    graph = defaultdict(list)

    for k in range(len(adj)):
        for i in range(len(adj[k])):
            w = cost[k][i]
            graph[k].append((w, adj[k][i]))

    q = [(0, s, ())]
    visited = set()
    min_dict = {s: 0}
    # (u, v, weight)
    # [(1,2,5), (2,5, 3)]

    while q:
        (costd,v1,path) = heappop(q)
        if v1 not in visited:
            visited.add(v1)
            path = (v1, path)
            if v1 == t:
                return costd

            for c, v2 in graph.get(v1, ()):
                if v2 in visited:
                    continue
                prev = min_dict.get(v2, None)
                next_item = costd + c
                if prev is None or next_item < prev:
                    min_dict[v2] = next_item
                    heappush(q, (next_item, v2, path))
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
