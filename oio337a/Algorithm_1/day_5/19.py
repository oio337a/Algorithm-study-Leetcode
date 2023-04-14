# 순회해서 길이를 구하고 n 만큼 적게 순환 돈뒤 다음 노드와 이어주기

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = start = head
        length = 1

        while end.next: # node 길이 재버리기
            end = end.next
            length += 1
        if length == 1 and n == 1: # 예외 처리 하나만있을 때
            head.val = ''
            return head
        if length - n == 0: # 예외 처리 제거할게 없을 때
            return head.next
        for _ in range(length - n - 1): # 순회하며 원하는 위치 찾기
            start = start.next
        start.next = start.next.next # 값 스킵하기
        return head
        