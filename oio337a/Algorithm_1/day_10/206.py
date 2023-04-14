# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		prev = None
		curr = head
		
		while curr:
			temp = curr.next  # temp 는 현재의 다음값 위치 저장
			curr.next = prev # 현재의 다음을 전의 포인터와 연결
			prev = curr # 전 포인터를 현재로 이동
			curr = temp # curr 값 다음으로 이동
		return prev