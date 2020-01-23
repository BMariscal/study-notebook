
[Link](https://www.hackerearth.com/practice/algorithms/graphs/strongly-connected-components/tutorial/)


* Adjacency Matrix vs Adjacency List:

    For a sparse graph (one in which most pairs of vertices are not connected by edges) an adjacency list 
    is significantly more space-efficient than an adjacency matrix (stored as an array): the space usage
     of the adjacency list is proportional to the number of edges and vertices in the graph, while for an
      adjacency matrix stored in this way the space is proportional to the square of the number of vertices.
       However, it is possible to store adjacency matrices more space-efficiently, matching the linear
        space usage of an adjacency list, by using a hash table indexed by pairs of vertices rather than
         an array.
         
     
     
* Connectivity:

    Connectivity in an undirected graph means that every vertex can reach every other vertex via any path. If the graph is not connected the graph can be broken down into Connected Components.
    
    Strong Connectivity (SCC) applies only to directed graphs. A directed graph is strongly connected if there is a directed path from any vertex to every other vertex. This is same as connectivity
     in an undirected graph, the only difference being strong connectivity applies to directed graphs and there should be directed paths instead of just paths. Similar to connected components,
      a directed graph can be broken down into Strongly Connected Components.
      
 https://www.youtube.com/watch?v=5wFyZJ8yH9Q           
1.  Do a  DFS on the original graph, keeping track of the finish times of each node. 
This can be done with a stack, when some  DFS finishes put the source vertex on the stack. This way node with highest finishing time will be on top of the stack.

2. Reverse the original graph, it can be done efficiently if data structure used to store the graph is an adjacency list.
3.  Do  DFS on the reversed graph, with the source vertex as the vertex on top of the stack. When DFS finishes, all nodes visited will form one Strongly Connected Component. If any more nodes remain unvisited, this means there are more Strongly Connected Component's, so pop vertices from top of the stack until a valid unvisited node is found. This will have the highest finishing time of all currently unvisited nodes. This step is repeated until all nodes are visited.