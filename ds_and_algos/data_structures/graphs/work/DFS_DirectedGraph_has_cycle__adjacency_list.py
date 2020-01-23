
"""
initiate visited and stack

if neighbor is in visited and stack, there's a cycle
"""


def dfs_cycle(adj, v, stack, visited):
    stack[v] = True
    visited[v] = True

    for w in adj[v]:
        if visited[w] == False:
            if dfs_cycle(adj, w, stack, visited) == True:
                return True
        elif stack[w] == True:
            return True

    stack[v] = False
    return False


def has_cycle(adj):
    stack = [False] * len(adj)
    visited = [False] * len(adj)

    for node in range(len(adj)):
        if visited[node] == False:
            if dfs_cycle(adj, node, stack, visited) == True:
                return True
    return False


a = [[1], [2], [0], [0]]  # 1, has cycle
print(has_cycle(a))

b = [[1, 2, 3], [2, 4], [3, 4], [], []]  # 0, does not have cycle
print(has_cycle(b))