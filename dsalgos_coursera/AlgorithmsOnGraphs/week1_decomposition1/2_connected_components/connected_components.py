#Uses python3

import sys

def visit(adj, x, visited):
    curr = adj[x]
    visited[x] = True

    for i in curr:
        if visited[i] is False:
            visit(adj,i, visited)

def number_of_components(adj):
    visited = [False] * len(adj)
    components = 0

    for j in range(len(adj)):
        if visited[j] is False:
            components+=1
            visit(adj, j, visited)

    return components

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
    print(number_of_components(adj))
