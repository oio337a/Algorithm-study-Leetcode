public class HouseRobber_198 {
    public int rob(int[] nums) {
        int len = nums.length;
        if (len == 1) return nums[0];
        int[] dp = new int[len];
        dp[0] = nums[0];
        dp[1] = nums[1] > nums[0] ? nums[1] : nums[0];
        for (int n = 2; n < len; n++)
            dp[n] = Math.max(dp[n-1], dp[n-2] + nums[n]);
        return dp[len - 1];
    }

    public static void main(String[] args) {
        HouseRobber_198 tmp = new HouseRobber_198();
        int[] houses = {2, 7, 9, 3, 2, 6, 5, 7, 4};
        System.out.println(tmp.rob(houses));
    }
}
// dp[n] = Math.max(dp[n-1], dp[n-2] + nums[n]);