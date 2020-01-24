#Uses python3

import sys

sys.setrecursionlimit(200000)

def DFS(adj, v, visited):
    visited[v] = True
    for i in adj[v]:
        if visited[i] == False:
            DFS(adj, i, visited)

def reverseG(adj):
    reversed_g = [[] for _ in range(len(adj))]
    for v in range(len(adj)):
        for adj_v in adj[v]:
            reversed_g[adj_v].append(v)
    return reversed_g


def visitEm(adj, v,visited, stack):
    visited[v]= True
    for i in adj[v]:
        if visited[i]==False:
            visitEm(adj, i, visited, stack)
    stack.append(v)

def number_of_strongly_connected_components(adj):
    result = 0
    stack = []

    visited = [False] * (len(adj))

    for i in range(len(adj)):
        if visited[i] == False:
            visitEm(adj, i, visited, stack)

    adj = reverseG(adj)

    visited = [False] * (len(adj))

    while stack:
        i = stack.pop()
        if visited[i] == False:
            DFS(adj, i, visited)
            result+=1

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
