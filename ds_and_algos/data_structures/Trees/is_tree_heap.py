# Check if a given Binary Tree is Heap
# Given a binary tree, we need to check it has heap property or not,
# Binary tree need to fulfill the following two conditions for being a heap –
#
# 1. It should be a complete tree (i.e. all levels except last should be full).
# 2. Every node’s value should be greater than or equal to its child node (considering max-heap).


# We check each of the above condition separately, for checking completeness isComplete and for checking heap isHeapUtil function are written.
# Detail about isComplete function can be found here.
#
# isHeapUtil function is written considering the following things –
#
# Every Node can have 2 children, 0 child (last level nodes) or 1 child (there can be at most one such node).
# If Node has No child then it’s a leaf node and returns true (Base case)
# If Node has one child (it must be left child because it is a complete tree) then we need to compare this node with its single child only.
# If the Node has both child then check heap property at Node at recur for both subtrees.
# Complete code.