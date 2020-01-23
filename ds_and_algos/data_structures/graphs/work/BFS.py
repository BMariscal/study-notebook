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