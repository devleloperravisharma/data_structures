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

root_node = Tree(8)
root_node.left = Tree(4)
root_node.right = Tree(2)
in_order_traversal(root_node)
