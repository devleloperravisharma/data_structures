class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root_node = Tree(8)
root_node.left = Tree(4)
root_node.right = Tree(2)

