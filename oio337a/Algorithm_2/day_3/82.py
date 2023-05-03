# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

# 못풀어서 좋은 풀이 함 가져와봤습니다.
class Solution: 
    def deleteDuplicates(self, head):
        # 더미 노드, 값을 저장할 pre, head 를 이동시킬 cur 셋팅
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            while cur.next and cur.val == cur.next.val: # 다른 부분이 있는 곳까지 루프
                cur = cur.next
            if pre.next == cur: # pre의 다음 값이 같다면 움직이지 x 다는 뜻
                pre = cur
            else: # 다르다면 while 문을 돌았다는 중복값 스킵하고 값 저장하기
                pre.next = cur.next
            cur = cur.next
        return dummy.next