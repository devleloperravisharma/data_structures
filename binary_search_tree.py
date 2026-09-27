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

def in_order_traversal(root):
    if root.left != None:
        in_order_traversal(root.left)

    print(root.value)

    if root.right != None:
        in_order_traversal(root.right)

def pre_order_traversal(root):
    print(root.value)

    if root.left != None:
        pre_order_traversal(root.left)

    if root.right != None:
        pre_order_traversal(root.right)

def post_order_traversal(root):
    if root.left != None:
        post_order_traversal(root.left)

    if root.right != None:
        post_order_traversal(root.right)

    print(root.value)

get_root_node = int(input("choose a number"))
root_node = less_than_or_greater(None, get_root_node)
ask_node_1 = int(input("choose a number "))
node1 = less_than_or_greater(root_node, ask_node_1)
#ask_node_2 = int(input("choose another number "))
#node2 = less_than_or_greater(root_node, ask_node_2)
# print(root_node.value)
# print(node1.value)
### printing in in order traversal
print("the numbers will be presented in the order of left node, root node, right node")
print("\n")
in_order_traversal(root_node)
print("\n")

### printing in pre order traversal
print("the numbers will be presented in the order of root node, left node, right node")
print("\n")
pre_order_traversal(root_node)
print("\n")

### printing in post order traversal
print("the numbers will be presented in the order of left node, right node, root node")
print("\n")
post_order_traversal(root_node)