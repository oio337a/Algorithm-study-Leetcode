# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        def isOk(r, s):
            if not r and not s:
                return True
            if not r or not s:
                return False
            if r.val == s.val and isOk(r.left, s.left) and isOk(r.right, s.right):
                return True
            else:
                return False
        if isOk(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        return False