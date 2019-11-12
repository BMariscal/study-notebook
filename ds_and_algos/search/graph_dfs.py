
# Create Stack => stack = myStack(5), where 5 is size of stack
# Functions of Stack => stack.push(int),stack.pop(),top(),isEmpty()
# class graph => {int vertices, linkedList[] array}
# class linkedList => {Node headNode}
# class Node => {int data, Node nextElement}
# Depth First Traversal of Graph "g" from source vertex
#
# my approach using a Stack
def dfsTraversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    stack = myStack(num_of_vertices)
    parso(g, source, stack)

    while stack.isEmpty() != True:
        v = stack.pop()
        result = str(v) + result
    return result


def parso(g, source, stack):
    stack.push(source)
    node = g.array[source].headNode
    while node != None:
        parso(g, node.data, stack)
        node = node.nextElement
    return


### other approach
def dfsTraversal(g,source):
  result = ""
  num_of_vertices = g.vertices
  #A list to hold the history of visited nodes
	#Make a node visited whenever you push it into stack
  visited = []
  for x in range(num_of_vertices):
    visited.append(False)
  #Create Stack(Implemented in previous lesson) for Depth First Traversal and Push source in it
  stack = myStack(num_of_vertices)
  stack.push(source)
  visited.insert(source,True)
  #Traverse while stack is not empty
  while (stack.isEmpty() == False):
    #Pop a vertex/node from stack and add it to the result
    current_node = stack.pop()
    result += str(current_node)
    #Get adjacent vertices to the current_node from the array,
		#and if they are not already visited then push them in the stack
    temp = g.array[current_node].headNode
    while (temp != None):
      if (visited[temp.data] == False):
        stack.push(temp.data)
        #Visit the node
        visited[temp.data] = True
      temp = temp.nextElement
  return result #For the above graph it should return "12453"

g = Graph(7)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(3,6)
print(dfsTraversal(g, 1))