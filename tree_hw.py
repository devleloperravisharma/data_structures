class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def in_order_traversal(root_node):
    if root_node.left != None:
        in_order_traversal(root_node.left)

    print(root_node.value)

    if root_node.right != None:
        in_order_traversal(root_node.right)


def pre_order_traversal(root_node):
    print(root_node.value)

    if root_node.left != None:
        pre_order_traversal(root_node.left)

    if root_node.right != None:
        pre_order_traversal(root_node.right)


def count_nodes(root_node):
    if root_node == None:
        return 0

    return 1 + count_nodes(root_node.left) + count_nodes(root_node.right)


root_node = Tree(10)
root_node.left = Tree(5)
root_node.right = Tree(15)

print("Inorder traversal:")
in_order_traversal(root_node)

print("Preorder traversal:")
pre_order_traversal(root_node)

print("Total number of nodes:")
print(count_nodes(root_node))
