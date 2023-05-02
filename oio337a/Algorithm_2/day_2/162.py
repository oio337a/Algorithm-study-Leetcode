from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return nums.index(max(nums))

nums = [1,2,1,3,5,6,4]
test = Solution()
print(test.findPeakElement(nums))