#Uses python3

import sys


def negative_cycle(adj, cost):
    distance_arr = [0] * len(adj)
    distance_arr[0] = 0

    for i in range(len(adj)):
        for u in range(len(adj)):
            for vertex in adj[u]:
                vertex_index = adj[u].index(vertex)
                if distance_arr[vertex] > distance_arr[u] + cost[u][vertex_index]:
                    distance_arr[vertex] = distance_arr[u] + cost[u][vertex_index]
                    if i == len(adj) - 1:
                        return 1
    return 0


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
    print(negative_cycle(adj, cost))
