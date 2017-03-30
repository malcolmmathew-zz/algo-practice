class Node:
    def __init__(self , key):
        self.data = key
        self.left = None
        self.right = None

def depth_binary_tree(cur_node):
    if (cur_node.left is None and cur_node.right is None):
        return 1

    if (cur_node.left is None):
        return depth_binary_tree(cur_node.right) + 1
    elif (cur_node.right is None):
        return depth_binary_tree(cur_node.left) + 1
    else:
        return min(depth_binary_tree(cur_node.right), depth_binary_tree(cur_node.left))+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print depth_binary_tree(root)
