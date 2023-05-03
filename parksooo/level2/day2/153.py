from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0
        e = len(nums) - 1
        m = 2147483647
        while (s <= e):
            mid = (s + e) // 2
            m = min(nums[s], nums[e], nums[mid], m) # 최솟값 찾기
            if nums[mid] > nums[s] and nums[mid] > nums[e]: # 미드값이 제일 클 때
                if nums[s] > nums[e]: # 스타트가 더 크다면
                    s = mid + 1
                else:
                    e = mid - 1
            else:
                if nums[s] > nums[e]:
                    e = mid - 1
                else:
                    s = mid + 1
        return m

test = Solution()
print(test.findMin([3,4,5,1,2]))

