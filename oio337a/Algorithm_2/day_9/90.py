from typing import List
from itertools import combinations

''' 모듈 활용한 풀이 '''
# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         result = [[]] # [] 아무것도 넣지 않은 빈 배열이 초기값
#         nums.sort() # 순서를 맞추기 위한 정렬 4,4,4,1,4,4,4 이런 경우 1,4 / 4,1 이 적용되어서 순서 맞춤
#         for i in range(len(nums)): # nums 만큼 반복
#             for j in map(list, combinations(nums, i + 1)): # 1개씩 증가하면서 combi 구하기
#                 if j not in result: # result에 해당 값이 없으면 
#                     result.append(j) # 해당 값 추가
#         return result

''' dfs 풀이 '''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path):
            nonlocal ans
            ans.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[i+1:], path+[nums[i]])
        ans = []
        dfs(sorted(nums), [])
        return ans

nums = [1,2,2]
test = Solution()
print(test.subsetsWithDup(nums))