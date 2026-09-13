class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def less_than_or_greater(root, insert):
    if root == None:
        root = Tree(insert)
    if root.value < insert:
        root.left = less_than_or_greater(root.left, insert)
    if root.value > insert:
        root.right = less_than_or_greater(root.right, insert)
    return root

root_node = less_than_or_greater(None, 50)

print(root_node.value)