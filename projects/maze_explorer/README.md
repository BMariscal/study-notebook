Maze explorer:
--


#### General Idea:


Concepts: graphs, trees, weights, recursion, search algorithms

A game to visualize different search algorithms, where a sprite image can write pixels on a board. 
These pixels will be the maze walls.
There's also a button that can automatically generate the maze with different patterns if users don't want to generate these themselves.
 
[Inspiration 1](https://www.cs.cmu.edu/~15110-n15/pa/pa1/index.html),
[Inspiration 2](https://clementmihailescu.github.io/Pathfinding-Visualizer/#)

#### Requirements:

---

* Display the time it took the algorithm to find the shortest path.
* Allow the user to run different algorithms on the same maze.
* Allow user to delete maze. 
* Allow the user to move the sprite image anywhere on the board before starting the game. 
* Once the algorithm the user selected finds the shortest path, the sprite image will move to maze's exit. 

Possible obstacles to spice things up for the search algorithms:

* Uncovered manholes, a city person's greatest threat! The manholes will become uncovered after the user presses `Start`, not before. 


#### Algorithms to use: 

---

* Dijkstra's Algorithm
* A*Search
* Greedy BFS
* BFS
* DFS



