# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import queue


def isValidBST(root):
    q = queue.Queue()
    q.put(root)

    while q.empty() == False:
        node = q.get()
        node_val = node.val

        if node.left != None:
            left_node = node.left
            left_node_val = left_node.val

            if left_node_val > node_val:
                return False

            q.put(left_node)

        if node.right != None:
            right_node = node.right
            right_node_val = right_node.val

            if right_node_val < node_val:
                return False
            q.put(right_node)

    return True


root = TreeNode(2)
node1 = TreeNode(1)
root.left = node1
root.right = TreeNode(3)
node1.left = TreeNode(5)

answer = isValidBST(root)
print(answer)
