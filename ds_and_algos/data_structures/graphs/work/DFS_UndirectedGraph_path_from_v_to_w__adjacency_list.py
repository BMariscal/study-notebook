def visit(adj, x,y, visited):

    if visited[x]:
        return
    if x == y:
        visited[x] = True
        return

    curr = adj[x]
    visited[x] = True

    for i in curr:
        visit(adj,i,y, visited)


def reach(adj, x, y):
    visited = [False] * len(adj)
    visit(adj, x,y, visited)
    return 1 if visited[y] else 0
