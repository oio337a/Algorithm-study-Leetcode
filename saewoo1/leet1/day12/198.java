class Solution {
    public int rob(int[] nums) {
        int maxMoney = 0;
        if (nums.length == 1)
            return nums[0];
        if (nums.length == 2)
            return Math.max(nums[0], nums[1]);
        maxMoney = getMoney(nums);
        return maxMoney;
    }
    private int getMoney(int[] nums) {
        int[] dp = new int[nums.length];
        int max = 0;
        dp[0] = nums[0];
        dp[1] = nums[1];
        dp[2] = nums[2] + nums[0];
        max = Math.max(dp[1], dp[2]);
        for (int i = 3; i < dp.length; i++) {
            // dp[i] = Math.max(nums[i] + dp[i - 2], nums[i] + dp[i - 3]);
            dp[i] = Math.max(dp[i - 2], dp[i - 3]) + nums[i];
            max = Math.max(max, dp[i]);
        }
        return max;
    }
}