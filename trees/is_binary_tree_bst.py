# Check if a binary tree is a binary search tree

class Node:
    def __init__(self , key):
        self.data = key
        self.left = None
        self.right = None

# Brute Force
def check_node(root):
# for each node, make sure its entire right subtree is greater, and its entire left subtree is less
    if root is None:
        return True

    is_balanced = ensure_right_balance(root.right, root.data) and ensure_left_balance(root.left, root.data)

    return is_balanced and check_node(root.left) and check_node(root.right)

def ensure_right_balance(node, value):

    if node is None:
        return True

    if node.data < value:
        return False

    return ensure_right_balance(node.right, value) and ensure_right_balance(node.left, value)

def ensure_left_balance(node, value):

    if node is None:
        return True

    if node.data > value:
        return False

    return ensure_left_balance(node.right, value) and ensure_left_balance(node.left, value)

# Second sol
def check_node2(root):

    if root is None:
        return True

    if check_left_tree_max(root.left, root.left.data) < root.data and check_right_tree_min(root.right, root.right.data) > root.data:
        return check_node(root.left) and check_node(root.right)
    else:
        print root.data
        return False

def check_left_tree_max(node, cur_max):

    if node is None:
        return

    cur_max =  max(node.data, cur_max)

    return  max(cur_max, check_left_tree_max(node.left, cur_max), check_left_tree_max(node.right, cur_max))

def check_right_tree_min(node, cur_min):

    if node is None:
        return

    cur_min = min(node.data, cur_min)

    return min(cur_min, check_left_tree_max(node.left, cur_min), check_left_tree_max(node.right, cur_min))

# Final Solution

def check_node3(root):

    return check_node_ranges(root, None, None)

def check_node_ranges(node, mini, maxi):

    if node is None:
        return True

    if ((mini is not None) and node.data < mini) or ((maxi is not None) and node.data > maxi):
        return False

    if !check_node_ranges(node.left, mini, node.data) or !check_node_ranges(node.right, node.data, maxi):
        return False

    return True




r = Node(15)
r.left = Node(7)
r.right   = Node(21);
r.left.left  = Node(6);
r.left.right = Node(10);
r.right.right = Node(24);
r.right.left   = Node(18);
r.right.left.right  = Node(20);


print check_node3(r)
