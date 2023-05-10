from typing import List
from itertools import combinations

''' 모듈 활용 풀이
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]] # [] 아무것도 넣지 않은 빈 배열이 초기값
        for i in range(len(nums)): # nums 만큼 반복
            for j in map(list, combinations(nums, i + 1)): # 1개씩 증가하면서 combi 구하기
                result.append(j) # 해당 값 추가
        return result
'''

''' 재귀 활용 풀이
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] # 반환할 정답 배열
        subset = [] # 값을 추가하고 뺄 배열

        def process(i):
            if i >= len(nums): # 탈출 조건
                res.append(subset.copy()) # 저장했던 subset 저장
                return
            
            subset.append(nums[i]) # index 1개씩 늘려가면서 subset append
            process(i + 1)

            subset.pop()
            process(i + 1)
        process(0)
        return res
'''
''' 개 쩌 는 풀 이 '''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [item+[num] for item in res]
            print(res)
        return res


nums = [1,2,3]
test = Solution()
print(test.subsets(nums))