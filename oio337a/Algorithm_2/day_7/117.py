
"""
# Definition for a Node.
"""
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: # root 가 없을 때 걍 None 리턴
            return root
        q = deque([root]) # queue 생성
        while q:
            size = len(q) # q의 level 수
            for i in range(size):
                node = q.popleft()
                if i < size - 1: # q의 끝 자락이면 다음 q의 첫번째 값 추가
                    node.next = q[0]
                if node.left: # 왼쪽 노드 추가
                    q.append(node.left)
                if node.right: # 오른쪽 노드 추가
                    q.append(node.right)
        return root