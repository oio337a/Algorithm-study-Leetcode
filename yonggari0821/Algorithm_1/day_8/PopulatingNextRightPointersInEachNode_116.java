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
}
public class PopulatingNextRightPointersInEachNode_116 {
    static void printTreeFront(Node root) // 전위순회
    {
        if (root.next == null) System.out.println(root.val + " #");
        else System.out.println(root.val + " " + root.next.val);
        if (root.left != null) printTreeFront(root.left);
        if (root.right != null) printTreeFront(root.right);
    }
    public Node connect(Node root) {
        if (root.left == null) return root;
        Node init = root;
        root.left.next = root.right;
        if (root.next != null) root.right.next = root.next.left;
        else root.right.next = null;
        connect(root.left);
        connect(root.right);
        return init;
    }

    public static void main(String[] args) {
        Node root1 = new Node(1);
        root1.left = new Node(2);
        root1.right = new Node(3);
        root1.left.left = new Node(4);
        root1.left.right = new Node(5);
        root1.right.left = new Node(6);
        root1.right.right = new Node(7);

        PopulatingNextRightPointersInEachNode_116 tmp = new PopulatingNextRightPointersInEachNode_116();
        tmp.connect(root1);
        printTreeFront(root1);
    }
}
