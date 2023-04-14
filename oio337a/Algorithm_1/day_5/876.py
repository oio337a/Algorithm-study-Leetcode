# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        pre_node = post_node = head # 다음 노드와, 전 노드 설정
        while pre_node and pre_node.next: # 다음 노드가 있는지 확인
            pre_node = pre_node.next.next # 다다음으로 이동
            post_node = post_node.next # 기준점 이동
        return post_node
    
"""
하나 이동하면 2개 이동하고
두번 이동하면 4개 이동하고
다음 바라보는것에 2배 더 이동해서 해당 노드 끝까지 이동하게 합니다.
"""