from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        l = len(nums)
        dp1 = [0 for i in range(l)]
        dp2 = [0 for i in range(l)]
        dp1[0] = nums[0]
        dp1[1] = max(nums[1], nums[0])
        for i in range(2, l):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
        dp2[1] = nums[1]
        dp2[2] = max(nums[1], nums[2])
        for i in range(2, l):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
        return max(dp1[l - 2], dp2[l - 1])


# class Solution1: 함수 만들어서 사용
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         if len(nums) == 2:
#             return max(nums[0], nums[1])
#         def helper(id, lens):
#             dp = [0 for i in range(lens)]
#             dp[id] = nums[id]
#             dp[id + 1] = max(nums[id], nums[id + 1])
#             for i in range(2, lens):
#                 dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
#             return dp[lens - 1]
#         return max(helper(0, len(nums) - 1), helper(1, len(nums)))

test = Solution()
print(test.rob([2, 3, 2]))