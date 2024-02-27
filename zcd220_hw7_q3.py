def is_height_balanced(bin_tree):
    return is_subtree_balanced(bin_tree.root)[1]


def is_subtree_balanced(node):
    if node is None:
        return 0, True
    left_height, left_balanced = is_subtree_balanced(node.left)
    right_height, right_balanced = is_subtree_balanced(node.right)

    if left_balanced and right_balanced and (abs(left_height - right_height) <= 1):
        balanced = True
    else:
        balanced = False
    height = max(left_height, right_height) + 1
    return (height, balanced)
