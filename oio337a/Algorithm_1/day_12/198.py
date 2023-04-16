from typing import List
import copy


class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        현재를 선택하거나, 저번 것을 계속 가거나
        '''
        n = len(nums)
        if not nums:
            return 0
        dp = copy.deepcopy(nums)
        for i in range(1, n):
            if i == 1:
                dp[1] = max(dp[0], dp[1])
            else:
                dp[i] = max(dp[i - 1], dp[i] + dp[i - 2])
        return dp[n - 1]


nums = [1, 2, 3, 3, 1, 6]
test = Solution()
print(test.rob(nums))
