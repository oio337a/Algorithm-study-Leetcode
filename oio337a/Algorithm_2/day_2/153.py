from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)


nums = [3,4,5,1,2]
test = Solution()
print(test.findMin(nums))