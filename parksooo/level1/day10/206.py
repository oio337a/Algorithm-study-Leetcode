from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # 반환할 list
        curr = head # 가지고 돌 curr

        while curr:
            next = curr.next # 다음을 변수에 저장
            curr.next = prev # 현재 다음을 prev로 저장한다 즉, prev를 하나씩 뒤로 밀면서 앞에 추가하는 것
            prev = curr # prev는 현재로 노드로 넣어놓는다
            curr = next # 리스트 순회
        return prev