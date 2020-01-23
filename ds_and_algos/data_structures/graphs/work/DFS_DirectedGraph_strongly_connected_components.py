

print("""
Checking Whether Any Intersection in a City
is Reachable from Any Other


Count the number of connected components in a Directed Graph

++++++++Directed Graph Strongly Connected Components++++++
\n
Compute the number of strongly connected components of a given directed graph with 𝑛 vertices and
𝑚 edges.


\n


1. initiliaze component count, dfs visit nodes, add nodes to visited, append nodes to stack
2. reverse graph
3. clear visited
4. pop nodes from stack, if not visited, add to component count
""")


def visitAll(graph, node, visited, stack):
    visited[node] = True
    for i in graph[node]:
        if visited[i] == False:
            visitAll(graph, i, visited, stack)
    stack.append(node)


def reverse(graph):
    new_graph = [[] for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in graph[i]:
            new_graph[j].append(i)
    return new_graph


def DFS(graph, node, visited):
    visited[node] = True
    for i in graph[node]:
        if visited[i] == False:
            DFS(graph, i, visited)


def strongly_connected(graph):
    component_count = 0
    stack = []
    visited = [False] * len(graph)

    for node in range(len(graph)):
        if visited[node] == False:
            visitAll(graph, node, visited, stack)

    graph = reverse(graph)
    visited = [False] * len(graph)

    while stack:
        i = stack.pop()
        if visited[i] == False:
            DFS(graph, i, visited)
            component_count += 1
    return component_count


a = [[1], [2], [0], [0]]
print(strongly_connected(a))  # 2

b = [[], [0], [1, 0], [2, 0], [1, 2]]
print(strongly_connected(b))  # 5
print("\n")