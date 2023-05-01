/* 뒤에서부터 n번째에 위치한 노드를 제거하세요 */

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int size = 0;
        for (ListNode node = head; node != null; node = node.next) // 노드 개수 세기
            size++;
        if (size == 1)
            return null;
        if (size == n)
            return head.next; // 여기까지 예외처리
        ListNode res = head;
        for (int i = 0; i < size - 1 - n; i++) { //뒤에서 n번째에 위치한 노드 전까지 위치하도록
            res = res.next;
        }
        res.next = res.next.next; // 제거할 노드를 그 다음 노드로 덮어 씌웁니다
        return head; // pointer로 이어졌으니 next로 이동하지 않은 첫 노드를 가리키는 head를 반환하도록
    }
}


-- slow, fast
다른 사람들 풀이인데 개짱천재임 이거보셈

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode fast = head, slow = head; // fast는 선발, slow는 후발
        /*
		 * 선발, 후발로 나뉘어 선발은 먼저 n만큼 달리고, null에 항상 먼저 닿는다
		 * 선발과 후발은 같은 속도로 움직이며 선발이 Null에 닿았을 때 후발이 위치한 값을 이용한다
		 * 시팔 이생각 어케했어 
		 */
        for (int i = 0; i < n; i++) { // 간격을 미리 벌려놓음
            fast = fast.next;
        }
        if (fast == null) {
            head = head.next;
            return head;
        }
        while (fast.next != null) {
            fast = fast.next;
            slow = slow.next;
        }
        slow.next = slow.next.next;

        return head;
    }
}