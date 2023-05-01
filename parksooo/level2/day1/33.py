from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s ,e = 0 ,len(nums) - 1
        while s <= e:
            mid = (s + e) // 2
            if nums[mid] == target:
                return mid
            if nums[s] <= nums[mid]: # 시작 값과 미드값을 비교한다 시작이 미드값보다 작으면
                if target < nums[s] or target > nums[mid]: # 미드 < 타겟 < 시작 값이면 s를 옮긴다
                    s = mid + 1
                else: # 아니면 엔드를 옮겨
                    e = mid - 1
            else:
                if target < nums[mid] or nums[e] < target: # 미드 < 타겟, 엔드 < 타겟 이면 e값을 옮긴다
                    e = mid - 1
                else:
                    s = mid + 1
        return -1

test = Solution()
print(test.search([4,5,6,7,0,1,2], 0))
print(test.search([1, 3], 3))