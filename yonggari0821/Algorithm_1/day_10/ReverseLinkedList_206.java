import java.util.Collections;
import java.util.Stack;

class ListNode2 {
    int val;
    ListNode2 next;
    ListNode2() {}
    ListNode2(int val) { this.val = val; }
    ListNode2(int val, ListNode2 next) { this.val = val; this.next = next; }
}

public class ReverseLinkedList_206 {
    // 스택 활용시 시간복잡도 쓰레기 => 다른 방법 찾아야 함
//    public ListNode2 reverseList(ListNode2 head) {
//        if (head == null) return null;
//        Stack<ListNode2> stack = new Stack<>();
//        while (head != null)
//        {
//            stack.push(new ListNode2(head.val));
//            head = head.next;
//        }
//        head = stack.pop();
//        ListNode2 output = head;
//        while (!stack.isEmpty())
//        {
//            head.next = stack.pop();
//            head = head.next;
//        }
//        return output;
//    }
    public ListNode2 reverseList(ListNode2 head)
    {
        if (head == null) return null;
        ListNode2 tmp = new ListNode2();
        ListNode2 lead = null;
        while(true)
        {
            tmp = head.next;
            head.next = lead;
            lead = head;
            head = tmp;
            if (head == null) break;
        }
        return lead;
    }

    public static void main(String[] args) {
        ReverseLinkedList_206 tmp = new ReverseLinkedList_206();
//        ListNode2 head = new ListNode2(1); // => 1
//        ListNode2 head = new ListNode2(1, new ListNode2(2)); // => 2 1
        ListNode2 head = new ListNode2(1, new ListNode2(2, new ListNode2(3, new ListNode2(4, new ListNode2(5))))); // => 5 4 3 2 1
        ListNode2 headToCheck = new ListNode2(1, new ListNode2(2, new ListNode2(3, new ListNode2(4, new ListNode2(5))))); // 반드시 동일한 값을 가지게 복붙해서 테스트 할 것!
        ListNode2 a = tmp.reverseList(head);
        while(headToCheck != null)
        {
            System.out.printf("%d / ", headToCheck.val);
            headToCheck = headToCheck.next;
        }
        System.out.println('\n'+"-----reversing-----");
        while(a != null)
        {
            System.out.printf("%d / ", a.val);
            a = a.next;
        }
    }
}
