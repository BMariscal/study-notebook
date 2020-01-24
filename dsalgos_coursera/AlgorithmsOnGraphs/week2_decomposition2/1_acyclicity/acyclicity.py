#Uses python3

import sys

def acyclic(adj):
    visited = [False] * len(adj)
    stack = [False] * len(adj)
    for node in range(len(adj)):
        if visited[node] == False:
            if acyclic_util(adj, node, visited, stack) == True:
                return 1
    return 0


def acyclic_util(adj, v, visited, stack):
    visited[v] = True
    stack[v] = True

    # If any neighbor is visited and in the stack then graph is cyclic
    for neighbor in adj[v]:
        if visited[neighbor] == False:
            if acyclic_util(adj, neighbor, visited, stack) == True:
                return True
        elif stack[neighbor] == True:
            return True

    stack[v] = False
    return False





if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
