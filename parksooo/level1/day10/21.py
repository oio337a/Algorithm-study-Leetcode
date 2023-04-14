from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    res = ListNode()
    curr = res
    while list1 and list2: #list 두개를 순회 하면서, val의 크기값을 비교하면서 curr에 넣어준다
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
           curr.next = list2
           list2 = list2.next
        curr = curr.next
    if list1: # 순회할때 리스트가 남아있는 것을 확인하기 위해서 넣어놈
        curr.next = list1
    elif list2:
        curr.next = list2
    return res.next #첫번째 노드는 dummy노드로 사용했기에 next를 반환

l1 = [1,2,4]
l2 = [1,3,4]
print(mergeTwoLists(any, l1, l2))