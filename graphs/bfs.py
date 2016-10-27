from Queue import Queue

class Node:
	def __init__(self, value):
		self.value = value
		self.connections = []

# Problem: Find path from Node a to b
def findPath(a, b):
	queue = Queue()
	queue.put(a)
	
	iter_val = b
	while not queue.empty():
		cur_node = queue.get()
		for con in cur_node.connections:

			if not hasattr(con, 'discovered'):
				con.parent = cur_node
				queue.put(con)
			if con == b:
				
				break;
		cur_node.discovered = True
	
	l =[b.value]

	while (iter_val is not a):
		
		l.append(iter_val.parent.value)
		iter_val = iter_val.parent

	l.reverse()
	return l



# Example graph
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")
i = Node("i")
a.connections.append(b)
a.connections.append(e)
b.connections.append(a)
b.connections.append(c)
b.connections.append(d)
b.connections.append(e)
c.connections.append(b)
d.connections.append(b)
d.connections.append(f)
d.connections.append(c)
d.connections.append(g)
e.connections.append(a)
e.connections.append(h)
f.connections.append(d)
g.connections.append(d)
g.connections.append(i)
h.connections.append(e)

print findPath(a, g)