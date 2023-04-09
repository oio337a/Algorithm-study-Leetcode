class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = ListNode(0)
        dum.next = head

        first = second = dum
        for _ in range(n):
            first = first.next
        while first and first.next:
            first = first.next
            second = second.next
        
        second.next = second.next.next

        return dum.next