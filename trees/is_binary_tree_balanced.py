class Node:
    def __init__(self , key):
        self.data = key
        self.left = None
        self.right = None

# Brute Force Solution
def is_tree_balanced(root):

    if root is None:
        return

    if (height(root.left) - height(root.right)) > 1:
        return False

    return is_tree_balanced(root.left) and is_tree_balanced(root.right)

def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

# Modified by storing height of each node
class NodeMod:
    def __init__(self , key):
        self.data = key
        self.left = None
        self.right = None
        self.height = None

def is_tree_balanced(root):
    if root is None:
        return

    if (height(root.left) - height(root.right)) > 1:
        return False

    return is_tree_balanced(root.left) and is_tree_balanced(root.right)

def height(root):
    if root.height is not None:
        return root.height
    if root is None:
        return 0
    root.height =  max(height(root.left), height(root.right)) + 1
    return root.height

# Optimal solution
class Node:
    def __init__(self , key):
        self.data = key
        self.left = None
        self.right = None

def check_tree_height(root):
    if root is None:
        return

    left_height = check_tree_height(root.left)
    if (left_height == -9999):
        return -9999

    right_height = check_tree_height(root.right)
    if (right_height == -9999):
        return -9999

    height_diff = abs(left_height - right_height)

    if (height_diff > 1):
        return -9999
    else:
        return max(left_height, right_height) + 1

def is_tree_balanced(root):
    return check_tree_height(root) != -9999
