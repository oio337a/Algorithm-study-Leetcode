from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        s = 0
        e = len(nums) - 1
        while (s < e):
            mid = (s + e) // 2
            if nums[mid] < nums[mid + 1]: # 큰지 판단하고 s 값을 갱신화
                s = mid + 1
            else:
                e = mid
        return s

test = Solution()
print(test.findPeakElement([1,6,5,4,3,2,1]))