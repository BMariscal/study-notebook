def lca(root, v1, v2):
  #Enter your code here
    if not root:
        return
    if root.info == v1 or root.info == v2:
        return root
    leftside = lca(root.left, v1, v2)
    rightside = lca(root.right, v1, v2)
    if not leftside:
        return rightside
    if not rightside:
        return leftside

    return root
