from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)

        def houserobber(money):
            dp = [0] * len(money)
            dp[0] = money[0]
            dp[1] = max(money[0], money[1])

            for i in range(2, len(money)):
                dp[i] = max(money[i] + dp[i - 2], dp[i - 1])
            return dp[-1]
        
        return max(houserobber(nums[:-1]),houserobber(nums[1:]) )

nums = [4,1,2,7,5,3,1]
test = Solution()
print(test.rob(nums))