#Uses python3

import sys
import queue

def bipartite(adj):
    visited = [False] * len(adj)
    visited[0] = True

    partition = [-1] * len(adj)
    partition[0] = 0
    q = queue.Queue()
    q.put(0)

    while q.empty() == False:
        v = q.get()
        for i in adj[v]:
            if partition[i] == partition[v]:
                return 0
            else:
                if visited[i] is False:
                    q.put(i)
                    partition[i] = 1 - partition[v]
                    visited[i] = True

    return 1



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
