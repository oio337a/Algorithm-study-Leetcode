from typing import List

def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(max[0], max[1])
    dp = [0 for _ in range(len(nums))]
    dp[0], dp[1] = nums[0], nums[1]
    dp[2] = nums[2] + dp[0]
    res = max(dp[1], dp[2])
    for i in range(3, len(nums)):
        dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i] # 점화식 
        res = max(dp[i], res)
    return res
print(rob([2, 1, 1, 2]))