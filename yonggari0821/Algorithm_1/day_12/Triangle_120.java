import java.util.ArrayList;
import java.util.List;

public class Triangle_120 {
    public int minimumTotal(List<List<Integer>> triangle) {
        int Max = triangle.size();
        if (Max == 1) return triangle.get(0).get(0);
        int[][] dp = new int[Max][Max];
        dp[0][0] = triangle.get(0).get(0);
        for (int r = 1; r < Max; r++)
        {
            for (int c = 0; c <= r; c++)
            {
                if (c == 0) dp[r][c] = dp[r-1][c] + triangle.get(r).get(0);
                else if (c == r) dp[r][c] = dp[r-1][c-1] + triangle.get(r).get(c);
                else dp[r][c] = Math.min(dp[r-1][c-1] , dp[r-1][c]) + triangle.get(r).get(c);
            }
        }
        int min = dp[Max - 1][0];
        for (int i = 1; i < Max; i++)
            min = min < dp[Max - 1][i] ? min : dp[Max - 1][i];
        return min;
    }

    public static void main(String[] args) {
        Triangle_120 tmp = new Triangle_120();
        List<List<Integer>> triangle = new ArrayList<>();
        List<Integer> line1 = new ArrayList<>();
        line1.add(2);
        List<Integer> line2 = new ArrayList<>();
        line2.add(3);
        line2.add(4);
        List<Integer> line3 = new ArrayList<>();
        line3.add(6);
        line3.add(5);
        line3.add(7);
        List<Integer> line4 = new ArrayList<>();
        line4.add(4);
        line4.add(1);
        line4.add(8);
        line4.add(3);
        triangle.add(line1);
        triangle.add(line2);
        triangle.add(line3);
        triangle.add(line4);
        System.out.println(tmp.minimumTotal(triangle));
    }
}
