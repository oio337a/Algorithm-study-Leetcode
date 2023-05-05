from typing import List
from functools import reduce

# time limit code
# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#       l = len(nums)
#       result = []
#       for i in range(l):
#          for step in range(l):
#             if nums[i:step+1]:
#               result.append(nums[i:step+1])
#       result = [i for i in result if reduce(lambda x, y: x * y, i) < k]
#       return len(result)


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        product = 1
        left = 0
        res = 0

        for right in range(len(nums)):
            product *= nums[right]
            while product >= k:
                product /= nums[left]
                left += 1
            res += right - left + 1

        return res

nums = [10,5,2,6]
k = 100
test = Solution()
print(test.numSubarrayProductLessThanK(nums, k))