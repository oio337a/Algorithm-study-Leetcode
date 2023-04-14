class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right)
      {
          this.val = val;
          this.left = left;
          this.right = right;
      }
}
public class MergeTwoBinaryTrees_617 {

    static void printTreeBack(TreeNode root) // 후위순회
    {
        if (root.left != null) printTreeBack(root.left);
        if (root.right != null) printTreeBack(root.right);
        System.out.println(root.val);
    }

    static void printTreeFront(TreeNode root) // 전위순회
    {
        System.out.println(root.val);
        if (root.left != null) printTreeFront(root.left);
        if (root.right != null) printTreeFront(root.right);
    }


    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if (root1 == null) return root2; // 둘 다 null이면 자동으로 null 반환
        if (root2 == null) return root1;
        // 여기까지 오면 둘 다 널이 아닌 상태 => 두 값의 합으로 노드 만들어야 함
        TreeNode tmp = new TreeNode(root1.val + root2.val);
        // 좌 우 자식 노드까지 만드는 것이 함수 안에 포함되어야 함
        // 이 때, 함수의 반환형을 잘 볼 것!
        tmp.left = mergeTrees(root1.left, root2.left);
        tmp.right = mergeTrees(root1.right, root2.right);
        return tmp;
    }


    public static void main(String[] args) {
        TreeNode root1 = new TreeNode(1);
        root1.left = new TreeNode(3);
        root1.left.left = new TreeNode(5);
        root1.right = new TreeNode(2);

        TreeNode root2 = new TreeNode(2);
        root2.left = new TreeNode(1);
        root2.left.right = new TreeNode(4);
        root2.right = new TreeNode(3);
        root2.right.right = new TreeNode(7);

        MergeTwoBinaryTrees_617 tmp = new MergeTwoBinaryTrees_617();
        TreeNode c = new TreeNode();
        c = tmp.mergeTrees(root1, root2);
        System.out.println("<Back>");
        printTreeBack(c);
        System.out.println("---------");
        System.out.println("<Front>");
        printTreeFront(c);
    }
}