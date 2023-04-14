
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None or root.left is None: # 현재가 없거나 왼쪽이 없을 때
            return root # 노드 끝 탐색 종료
        root.left.next = root.right # 왼쪽의 다음은 오른쪽
        if root.next: # 내 옆 노드가 있을 때
            root.right.next = root.next.left # 자식 노드 이어주기 
        self.connect(root.left)
        self.connect(root.right)
        return root