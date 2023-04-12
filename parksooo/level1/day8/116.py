from typing import Optional
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
	if root is None:
		return None
	q = deque([root])

	while q: 
		size = len(q)
		while size > 0:
			node = q.popleft()
			if size > 1 :
				node.next = q[0]
				print(q[0])
			size -= 1
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)
	return root
