from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue #전의 요소랑 다른지 확인하고 같으면 중복이니 for문을 넘어간다
            left, right = i + 1, len(nums) - 1 # i기준으로 왼쪽 오른쪽 설정
            while left < right: # 돌면서 리스트 만들어서 append
                arr = [nums[left], nums[i], nums[right]]
                if sum(arr) < 0:
                    left += 1 # 0보다 작다면 커져야 하기에 왼쪽을 더해준다
                elif sum(arr) > 0:
                    right -= 1 
                else :
                        arr.sort()
                        res.append(arr)
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1 # 중복값 제거 
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return res
test = Solution()
print(test.threeSum([-1,0,1,2,-1,-4]))