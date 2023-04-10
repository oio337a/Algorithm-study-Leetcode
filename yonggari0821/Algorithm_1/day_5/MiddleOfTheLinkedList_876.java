import java.util.ArrayList;

class ListNode1 {
    int val;
    ListNode1 next;
    ListNode1() {}
    ListNode1(int val) { this.val = val; }
    ListNode1(int val, ListNode1 next) { this.val = val; this.next = next; }
 }

public class MiddleOfTheLinkedList_876 {
    public ListNode1 middleNode(ListNode1 head) {
        if (head.next == null) return head;
        ArrayList<ListNode1> nodeList = new ArrayList<>();
        while (head != null)
        {
            nodeList.add(head);
            head = head.next;
        }
        System.out.println(nodeList.size());
        return nodeList.get(nodeList.size() / 2);
    }

    public ListNode1 middleNodeByTwoPointer(ListNode1 head)
    {
        ListNode1 middle = head;
        ListNode1 right = head;
        while (true)
        {
            if (right == null || right.next == null) break;
            middle = middle.next;
            right = right.next.next;
        }
        return middle;
    }

    public static void main(String[] args) {
        MiddleOfTheLinkedList_876 tmp = new MiddleOfTheLinkedList_876();
        ListNode1 head = new ListNode1(1, new ListNode1(2, new ListNode1(3, new ListNode1(4, new ListNode1(5, new ListNode1(6))))));
        System.out.println(tmp.middleNode(head).val);
    }
}
