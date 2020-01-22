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




graph = [[1,2,4],[2,3],[],[4],[0]]
print(number_of_components(graph))