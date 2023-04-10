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