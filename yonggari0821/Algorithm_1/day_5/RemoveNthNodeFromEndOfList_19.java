class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
public class RemoveNthNodeFromEndOfList_19 {
    /*
    1 2
    1 => 1
    2 => 2
    1 2 3 4 5
    1 => 1 2 3 4
    2 => 1 2 3 5
     */
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int i = 0;
        int j = -1 * n - 1;
        ListNode out = head;
        ListNode tmp = out;
        while (head != null)
        {
            i++;
            j++;
            head = head.next;
            if (j > 0) out = out.next;
        }
        if (i == 1) return null;
        else if (j == -1) tmp = tmp.next;
        out.next = out.next.next;
        return tmp;
    }

    /**
     *       Time complexity  - O(m) [O(m) + O(m-1) + O(n) ~ O(m)]
     *                               [O(m) = for reverse, O(m-1) = for reverse after deletion, O(n) = for finding the nth node to delete]
     *       Space complexity - O(1)
     * */

    // 다른 분이 작성한 코드 : while 문 부분이 잘 이해 안 됨.
    public ListNode removeNthFromEndByReverse(ListNode head, int n) {
        ListNode reverseHead = reverse(head);

        ListNode prevNode = null;
        ListNode currNode = reverseHead; // node to be deleted
        ListNode nextNode = null;
        n--;

        while(n > 0) {
            nextNode = currNode.next;
            prevNode = currNode;
            currNode = nextNode;
            n--;
        }

        if(prevNode == null) {
            reverseHead = reverseHead.next;
        } else {
            prevNode.next = currNode.next;
        }
        currNode.next = null;

        return reverse(reverseHead);
    }

    private ListNode reverse(ListNode head) {
        if(head == null) {
            return null;
        }

        ListNode prevNode = null;
        ListNode currNode = head;
        ListNode nextNode = null;

        while(currNode != null) {
            nextNode = currNode.next; // a = b;
            currNode.next = prevNode; // b = c;
            prevNode = currNode; // c = d;
            currNode = nextNode; // d = a;
        } // Reverse By rotating way => space Complexity O(2)

        return prevNode;
    }

    public static void main(String[] args) {
        RemoveNthNodeFromEndOfList_19 tmp = new RemoveNthNodeFromEndOfList_19();
//        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, new ListNode(6))))));
        ListNode head = new ListNode(1, new ListNode(2));
//        System.out.println(tmp.removeNthFromEnd(head, 2).val);
//        System.out.println(tmp.removeNthFromEnd(head, 2).next.val);
//        System.out.println(tmp.removeNthFromEnd(head, 2).next.next.val);
//        System.out.println(tmp.removeNthFromEnd(head, 2).next.next.next.val);
//        System.out.println(tmp.removeNthFromEnd(head, 2).next.next.next.next.val); // 6
        System.out.println(tmp.removeNthFromEnd(head, 1).val); // 6
    }
}

//123456
//n = 2
//12346
