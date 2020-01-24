"""
An undirected graph is called bipartite if its vertices can be split into two parts such that each edge of the
graph joins to vertices from different parts. Bipartite graphs arise naturally in applications where a graph
is used to model connections between objects of two different types (say, boys and girls; or students and
dormitories).
An alternative definition is the following: a graph is bipartite if its vertices can be colored with two colors
(say, black and white) such that the endpoints of each edge have different colors.


Given an undirected graph with 𝑛 vertices and 𝑚 edges, check whether it is bipartite.

https://www.educative.io/edpresso/what-is-a-bipartite-graph


	// Create a color array to store colors
	// assigned to all veritces. Vertex
	// number is used as index in this array.
	// The value '-1' of colorArr[i]
	// is used to indicate that no color
	// is assigned to vertex 'i'. The value 1
	// is used to indicate first color
	// is assigned and value 0 indicates
	// second color is assigned.


"""


def bipartite(adj):
    visited = [False] * len(adj)
    visited[0] = True

    partition = [-1] * len(adj)
    partition[0] = 0
    q = queue.Queue()
    q.put(0)

    while q.empty() == False:
        v = q.get()
        for i in adj[v]:
            if partition[i] == partition[v]:# if color of vertex == color of neighbor, then the graph is not bipartite
                return 0
            else:
                if visited[i] is False:
                    q.put(i)
                    # Assign alternate color to this adjacent v of u
                    partition[i] = 1 - partition[v] # 1 - 0 = 1
                                                    #
                    visited[i] = True

    return 1
