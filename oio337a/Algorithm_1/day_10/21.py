# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		
		head = ListNode(-1) # 새로운 노드 생성
		cursor = head # 이동할 커서 생성
		
		while list1 and list2: # list1, list2 가 없을 때 까지 반복
			if list1.val <= list2.val: # list1의 값이 list2의 값보다 작거나 같다면
				cursor.next = list1 # 커서의 다음을 list 1으로 설정 
				list1 = list1.next # list1 다음 값으로 이동
			else:
				cursor.next = list2 # list2의 값 이어주기
				list2 = list2.next # 다음값으로 이동
			cursor = cursor.next # 커서 이동
		if list1:
			cursor.next = list1 # list1 이 남아있다면 다음값들 이어주기
		else:
			cursor.next = list2 # list2 이 남아있다면 다음값들 이어주기
		return head.next # 시작값 반환