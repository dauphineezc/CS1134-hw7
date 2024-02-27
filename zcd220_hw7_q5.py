from LinkedBinaryTree import LinkedBinaryTree


def create_expression_tree(prefix_exp_str):
    nodes = prefix_exp_str.split()
    tree, pos = create_expression_tree_helper(nodes, 0)
    return tree


def create_expression_tree_helper(nodes, start_pos):
    root_node = nodes[start_pos]
    if root_node.isdigit():
        root = int(root_node)
        subtree = LinkedBinaryTree(LinkedBinaryTree.Node(root))
        return subtree, 1

    root = root_node
    left, left_size = create_expression_tree_helper(nodes, start_pos + 1)
    right, right_size = create_expression_tree_helper(nodes, start_pos + 1 + left_size)
    tree = LinkedBinaryTree(LinkedBinaryTree.Node(root, left.root, right.root))

    return tree, 1 + left_size + right_size


def prefix_to_postfix(prefix_exp_str):
    tree = create_expression_tree(prefix_exp_str)

    postfix_list = []
    for node in tree.postorder():
        postfix_list.append(str(node.data))

    postfix_str = ' '.join(postfix_list)
    return postfix_str
