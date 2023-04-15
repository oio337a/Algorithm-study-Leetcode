class ListNode {
    int val;
    ListNode2 next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode2 next) { this.val = val; this.next = next; }
}

public class MergeTwoSortedLists_21 {
    public ListNode2 mergeTwoLists(ListNode2 list1, ListNode2 list2)
    {
        if (list1 == null && list2 == null) return null; // 둘 다 null이면 그냥 바로 null 반환
        ListNode2 list3 = new ListNode2(); // 최종적으로 반환할 리스트의 헤드 노드 => 따로 빼둬야 함!
        ListNode2 tmp = list3;
        while (!(list1 == null && list2 == null)) // 둘 다 null인 경우만 아니면 계속 배정할 값이 남아 있음
        {
            if (list1 != null && list2 != null) // 둘 다 null이 아님 => 비교 필요 => 더 작은 쪽으로 배정하고 해당 리스트 다음으로 넘기기
            {
                if (list1.val >= list2.val)
                {
                    tmp.val = list2.val;
                    list2 = list2.next;
                }
                else
                {
                    tmp.val = list1.val;
                    list1 = list1.next;
                }
            }
            // 한 쪽이 null인 경우 => null이 아닌 쪽을 배정하고 해당 리스트 다음으로 넘기기
            else if (list1 == null)
            {
                tmp.val = list2.val;
                list2 = list2.next;
            }
            else if (list2 == null)
            {
                tmp.val = list1.val;
                list1 = list1.next;
            }
            if (list1 == null && list2 == null) break; // 여기서 둘 다 null인지를 else가 아니라 if로 다시 한 번 체크해서 break 해줘야 함!
            // 그래야 아래 부분이 적절하게 생략되서 마지막에 빈 노드가 붙어나오지 않음!
            tmp.next = new ListNode2();
            tmp = tmp.next;
        }
        return list3;
    }

    public static void main(String[] args) {
        MergeTwoSortedLists_21 tmp = new MergeTwoSortedLists_21();
        // case 1
        ListNode2 list1 = new ListNode2(1, new ListNode2(2, new ListNode2(4)));
        ListNode2 list2 = new ListNode2(1, new ListNode2(3, new ListNode2(4)));
        // case 2 - 1, 2 - 2
//        ListNode list1 = null;
//        ListNode list2 = null;
//        ListNode list2 = new ListNode(0);

        ListNode2 list3 = tmp.mergeTwoLists(list1, list2);
        while (list3 != null)
        {
            System.out.println(list3.val);
            list3 = list3.next;
        }
    }
}
