from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        dq = deque()
        dq.append(root)
        dum = Node(-111)
        while dq:
            l = len(dq)
            prev = dum
            for i in range(l):
                poped = dq.popleft()
                if poped.left:
                    dq.append(poped.left)
                    prev.next = poped.left
                    prev = prev.next
                if poped.right:
                    dq.append(poped.right)
                    prev.next = poped.right
                    prev = prev.next
        return root


