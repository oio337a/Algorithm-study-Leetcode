from typing import List

# -- Combination을 이용한 브루트포스 풀이
# from itertools import combinations
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) < 3:
#             return []
#         else:
#             answer = []
#             combi = list(combinations(nums, 3))
#             for element in combi:
#                 if sum(element) == 0:
#                     temp = sorted(list(element))
#                     if temp not in answer:
#                         answer.append(temp)

#             return answer

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort() # 포인터 알고리즘을 위한 정렬

        for i in range(len(nums) - 2): # 2개 전까지 반복
            if i > 0 and nums[i] == nums[i - 1]: # 전에 값이 같으면 패스
                continue
            left = i + 1 # 왼쪽 포인터 세팅
            right = len(nums) - 1 # 오른쪽 포인터 세팅

            while left < right: # 왼쪽이 오른쪽을 넘지 않는 경우까지 반복
                sum_temp = nums[i] + nums[left] + nums[right] # 값 더하기
                if sum_temp < 0: # 더한 값이 음수 이면 왼쪽 오른쪽으로 이동
                    left += 1
                elif sum_temp > 0: # 더한 값이 양수이면 오른쪽 왼쪽으로 이동
                    right -= 1
                else: # 0인 경우
                    answer.append([nums[i], nums[left], nums[right]]) # 값 추가

                    while left < right and nums[left] == nums[left + 1]: # 같은 값이 있으면 스킵
                        left += 1
                    while left < right and nums[right] == nums[right - 1]: # 같은 값이 있으면 스킵
                        right -= 1
                    left += 1 # 왼쪽 오른쪽 이동
                    right -= 1 # 오른쪽 왼쪽 이동

        return answer


nums = [-1,0,1,2,-1,-4]
test = Solution()
print(test.threeSum(nums))