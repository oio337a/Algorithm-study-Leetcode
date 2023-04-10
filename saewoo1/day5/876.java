/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next; // node, next를 지닌 연결 리스트
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        int count = size(head) / 2;
		/* 주어진 head를 넣어서 몇개가 들어있는 연결 리스트인지 알게 되엇습니다
			이걸 반으로 나누면 가운데 지점이 되겠져? 짝수면 딱 나눠지고, 홀수면 1이 남지만 두번 째를 기준으로 한다 했으니 짝수와 동일하게 취급해도 됩니다
		*/
        int i = 0;
        while (i++ < count && head != null) { // head를 직접 mid 지점까지 밀고, 반환하면 끗!
            head = head.next;
        }
        return head;
    }

    public int size(ListNode head) { // 길이를 구하기 위해 node를 순회하면서 개수를 세줍니당
        int size = 0;
        for (ListNode n = head; n.next != null; n = n.next)
            size++;
        return size + 1; // 개수로 인지하기 위해 마지막에 1을 더했슴
    }
}