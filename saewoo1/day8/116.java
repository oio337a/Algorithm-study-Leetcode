/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

/* perfect binary tree니까 왼쪽이 있으면 무죅건 오른족이 있다
left의 next node를 right로 계속해서 연결하고, 마지막에 닿았을 때 null을 연결해주면 되는 문제
*/
class Solution {
    public Node connect(Node root) {
        if (root == null)
            return root;
        if (root.left != null) // 좌츠깅 있다 == 우측도 있다
            root.left.next = root.right; // left의 next 노드를 보장받은 right로 연결하자
        if (root.right != null && root.next != null) // right에 길이 있고, 아래로 내려갈 수 있다면
            root.right.next = root.next.left; // 끝에 닿을 때까지 계속해서 right의 우측을 연결해준다
        connect(root.left);
        connect(root.right);
        return root;
    }
}