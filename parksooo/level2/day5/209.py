import sys
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target == 0:
            return 0
        j, res = 0, 2147483647
        p, l_n = 0, len(nums)

        for i in range(l_n):
            p += nums[i]
            while p >= target:
                res = min(res, i - j + 1)
                p -= nums[j]
                j += 1
        return res if res != 2147483647 else 0 #더하고 뺴면서 갯수를 구하자!

test = Solution()
print(test.minSubArrayLen(7, [2,3,1,2,4,3]))
print(test.minSubArrayLen(11, [1,1,1,1,1,1]))