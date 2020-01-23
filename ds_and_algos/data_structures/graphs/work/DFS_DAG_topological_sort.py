"""
when you are sure that there are no cyclic dependencies in the given graph
"""

print(
    """++++++++++++ Topological sort:

    Elements without dependencies first.
    Least dependencies ...to more dependencies.

    """)


def toposort(adj):
    order_list = []
    visited = [False] * len(adj)

    for node in range(len(adj)):
        if visited[node] == False:
            dfs_sort(adj, node, order_list, visited)
    return order_list


def dfs_sort(adj, v, order_list, visited):
    visited[v] = True

    for w in adj[v]:
        if visited[w] == False:
            dfs_sort(adj, w, order_list, visited)

    order_list.insert(0, v)


a = [[1], [], [0], [0]]
print(toposort(a), end="  Expect: 3,2,0,1   \n")  # 3,2,0,1

b = [[], [], [0], []]
print(toposort(b), end="   Expect: 1,2,0,3  or 3,2,1,0 \n")  # 1,2,0,3

c = [[], [0], [1, 0], [0, 2], [1, 2]]
print(toposort(c), end="  Expect: 4,3,2,1,0  \n ")  # 4,3,2,1,0

print(" \n \n \n")