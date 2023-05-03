from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode() # 결과 노드
        res.next = head # 더미 다음을 헤드로 선언
        pre = res # pre 전의 노드에 대한 탐색
        curr = head # 현재

        while curr:
            if curr.next and curr.val == curr.next.val: # 현재와 다음을 val이 같다면 다를 때 까지 while을 돌린다
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                pre.next = curr.next #pre를 현재 다음으롤 넣는다
            else:
                pre = curr # 그렇지 않다면 그냥 pre 에 현재를 넣는다
            curr = curr.next # 현재 노드 이동
        return res.next

test = Solution()
print(test.deleteDuplicates(n))

