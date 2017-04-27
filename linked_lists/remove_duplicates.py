class Node:
    __init__(self, key):
        self.data = key
        self.next = None

def remove_duplicates(head):
    s = set()
    s.add(head.data)
    n = head
    prev = head
    cur = head.next
    while (cur.next is not None):
        if cur.data in s:
            prev.next = cur.next
            cur = cur.next
        else:
            cur = cur.next
            s.add(cur)
            prev = prev.next

    return n
