def min_and_max(bin_tree):
    if len(bin_tree) == 0:
        raise Exception("Tree is empty")
    return subtree_min_and_max(bin_tree.root)


def subtree_min_and_max(root):
    if root.left is None and root.right is None:
        return (root.data, root.data)
    elif root.left is None:
        right_min, right_max = subtree_min_and_max(root.right)
        return (min(root.data, right_min), max(root.data, right_max))
    elif root.right is None:
        left_min, left_max = subtree_min_and_max(root.left)
        return (min(root.data, left_min), max(root.data, left_max))
    else:
        left_min, left_max = subtree_min_and_max(root.left)
        right_min, right_max = subtree_min_and_max(root.right)
        return (min(root.data, left_min, right_min), max(root.data, left_max, right_max))

