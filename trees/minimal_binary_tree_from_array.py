class Node:
    def __init__(self , key):
        self.data = key
        self.left = None
        self.right = None

def minimal_subtree(array):

    if (len(array) ==0):
        return None

    mid_val = len(array)/2

    root_node = new Node(array[mid_val])

    left_array = [0:mid_val]
    right_array = [mid_val+1:len(array)]

    root_node.left = minimal_subtree(left_array)
    root_node.right = minimal_subtree(right_array)

    return root_node
