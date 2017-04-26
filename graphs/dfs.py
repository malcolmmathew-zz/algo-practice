class Node:
	def __init__(self, value):
		self.value = value
		self.connections = []
        self.visited  = False

def dfs(root, dest_val):
    if (root is None):
        return False

    if root == dest_val:
        return True

    root.visited = True

    isFound = False
    for adj in root.connections:
        if adj.visited:
            continue
        else:
            if dfs(adj):
                return True

    return False
