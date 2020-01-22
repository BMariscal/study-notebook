* Adjacency Matrix vs Adjacency List:

For a sparse graph (one in which most pairs of vertices are not connected by edges) an adjacency list 
is significantly more space-efficient than an adjacency matrix (stored as an array): the space usage
 of the adjacency list is proportional to the number of edges and vertices in the graph, while for an
  adjacency matrix stored in this way the space is proportional to the square of the number of vertices.
   However, it is possible to store adjacency matrices more space-efficiently, matching the linear
    space usage of an adjacency list, by using a hash table indexed by pairs of vertices rather than
     an array.