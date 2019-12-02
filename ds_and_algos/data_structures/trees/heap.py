# Array representation

class MinIntHeap:
    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.items = [0] *  self.capacity

    def getLeftChildIndex(self, parentIndex):
        return 2 * parentIndex + 1

    def getRightChildIndex(self, parentIndex):
        return 2 * parentIndex + 2

    def getParentIndex(self, childIndex):
        return (childIndex - 1) // 2

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0


    def leftChild(self, index):
        return self.items[self.getLeftChildIndex(index)]


    def rightChild(self, index):
        return self.items[self.getRightChildIndex(index)]


    def parent(self, index):
        return self.items[self.getParentIndex(index)]



    def swap(self, indexOne, indexTwo):
        temp = self.items[indexOne]
        self.items[indexOne] = self.items[indexTwo]
        self.items[indexTwo] = temp

    def ensureExtraCapacity(self):

        if (self.size == self.capacity):
            new_arr = [0] *  self.capacity
            self.item = (self.item[0:]) +  new_arr
            self.capacity *= 2


    def peek(self):
        return self.items[0]



## arr = [100, 20, 50, 10, 5, 25, 23]
## parent: i //2 .. for instance, child @ index 3's parent is 3//2 is located at index 1
## left_child: (2*i)
## right_child: (2* i) + 1

