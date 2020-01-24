print("+++++++++++++++++BFS++++++++++++++++")

from collections import deque


def bfs(graph, root):
    visited = set()
    queue = deque([root])
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited


c = [[1, 2], [2], []]
print(bfs(c, 0))

a = [[1], [2], [0], [0]]
print(bfs(a, 0))

b = [[4], [0], [1, 0], [2, 0], [1, 2]]
print(bfs(b, 0))

print("\n")



from collections import deque


def bfs(graph, root, target):
    visited = set()
    queue = deque([root])
    total = 0
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                total += neighbour
                if total <= target:
                    visited.add(neighbour)
                    queue.append(neighbour)
                else:
                    return visited, total
    return visited, total


c = [[1, 2], [2], []]
print(bfs(c, 0, 3))

a = [[1], [2], [0], [0]]
print(bfs(a, 0, 3))

b = [[4], [0], [1, 0], [2, 0], [1, 2]]
print(bfs(b, 0, 10))

from collections import deque


def bfs(graph, root):
    visited = set()
    queue = deque([root])
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited


c = [[1, 2], [2], []]
print(bfs(c, 0))

a = [[1], [2], [0], [0]]
print(bfs(a, 0))

b = [[4], [0], [1, 0], [2, 0], [1, 2]]
print(bfs(b, 0))


""""
https://courses.grainger.illinois.edu/cs225/fa2019/resources/bfs-dfs/

"""

print("++++++++++++BFS II+++++++++++++++")

"""
Given an undirected graph with 𝑛 vertices and 𝑚 edges and two vertices 𝑢 and 𝑣, compute the length
of a shortest path between 𝑢 and 𝑣 (that is, the minimum number of edges in a path from 𝑢 to 𝑣).

"""

def bfs(adj, s, t):
    n = len(adj)
    dist = [-1] * n
    dist[t] = 0
    queue = []
    queue.append(s)

    while queue:
        v = queue.pop(0)
        for u in adj[v]:
            if dist[u] == -1:
                queue.append(u)
                dist[u] = dist[v] + 1

    return dist[s]


s = 1
t = 3
c = [[1], [2], [0], [0]]
print(bfs(c, s, t))

b = [[3, 4], [], [3], [], [1]]
s = 2
t = 4
print(bfs(b, s, t))

print("\n")