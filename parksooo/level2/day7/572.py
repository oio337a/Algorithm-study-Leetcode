from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def checkSame(r, s) -> bool: # 재귀를 통해서 노드를 탐색한다
            if not r and not s:
                return True
            if not r or not s:
                return False
            if r.val == s.val and checkSame(r.left, s.left) and checkSame(r.right, s.right): # 지금의 val이 같으면 오른쪽 왼쪽을 다시 탐색한다
                return True
            else :
                return False
        if checkSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot): # 어느부분부터 sub인지 판단하기 위해 root 부터 왼쪽 오른쪽 다 확인한다
            return True
        else :
            return False