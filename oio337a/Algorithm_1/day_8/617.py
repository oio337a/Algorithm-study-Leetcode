# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2: # root1, root2 의 값이 모두 존재할 때
            node = TreeNode(root1.val + root2.val) # 새로운 노드 1, 2 값 더해서 생성
            node.left = self.mergeTrees(root1.left, root2.left) # left 재귀
            node.right = self.mergeTrees(root1.right, root2.right) # right 재귀
            return node # node 반환 (재귀가 풀리면서 시작했던 시작 노드 반환)
        else:
            return root1 or root2 # or 연산 root1 이 존재하면 root1 반환 없을 때 root2 반환