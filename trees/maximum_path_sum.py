class Node:
    def __init__(self , key):
        self.data = key
        self.left = None
        self.right = None

def max_path_sum(cur_node):
    if cur_node is None:
        return 0
    left_max = max_path_sum(cur_node.left)
    right_max = max_path_sum(cur_node.right)

    one_max = max(cur_node.data+left_max, cur_node.data+right_max)
    two_max = max(cur_node.data, cur_node.data + left_max+right_max)
    max_path_sum.a = 
    return max(one_max, two_max)

# Driver program
root = Node(10)
root.left = Node(2)
root.right   = Node(10);
root.left.left  = Node(20);
root.left.right = Node(1);
root.right.right = Node(-25);
root.right.right.left   = Node(3);
root.right.right.right  = Node(4);
print "Max path sum is " ,max_path_sum(root);
