public class ClimbingStairs_70 {
    static int[] dp;
    public int climbStairs(int n) {
        dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        if (dp[n] != 0) return dp[n];
        else
        {
            for (int i = 2; i <= n; i++)
            {
                dp[i] = dp[i - 1] + dp[i - 2];
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        ClimbingStairs_70 tmp = new ClimbingStairs_70();
        int n = 45; // 46부터는 int형 범위 벗어남!
        System.out.println(tmp.climbStairs(n)); // 1836311903 약 18억
    }
}

// 1 2 3 5 8 => 피보나치
