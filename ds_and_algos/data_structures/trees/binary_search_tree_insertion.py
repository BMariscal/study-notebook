class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Node is defined as
    # self.left (the left child of the node)
    # self.right (the right child of the node)
    # self.info (the value of the node)
    def insert_helper(self, cur, val):
        if not cur:
            cur = Node(val)
        elif cur.info > val:
            cur.left = self.insert_helper(cur.left, val)
        else:
            cur.right = self.insert_helper(cur.right, val)

        return cur

    def insert(self, val):
        # Enter you code here.

        if self.root == None:
            self.root = Node(val)

        else:
            self.insert_helper(self.root, val)

