def bfsTraversal(g,source):
  result = ""
  num_of_vertices = g.vertices
    #Alist to hold the history of visited nodes
	#Make a node visited whenever you enqueue it into queue
  visited = []
  for i in range(num_of_vertices):
    visited.append(False)
  #Create Queue(implemented in previous lesson) for Breadth First Traversal and enqueue source in it
  queue = myQueue()
  queue.enqueue(source)
  visited.insert(source,True)
 #Traverse while queue is not empty
  while(queue.isEmpty() == False):
  #Dequeue a vertex/node from queue and add it to result
   current_node = queue.dequeue()
   result += str(current_node)
    #Get adjacent vertices to the current_node from the list,
	#and if they are not already visited then enqueue them in the Queue
   temp = g.array[current_node].headNode
   while (temp != None):
    if(visited[temp.data] == False):
      queue.enqueue(temp.data)
      visited[temp.data] = True #Visit the current Node
    temp = temp.nextElement
  return result

g = Graph(6)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(2,3)

print(bfsTraversal(g, 0))