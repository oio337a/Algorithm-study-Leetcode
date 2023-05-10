from typing import List
from itertools import combinations

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.DFS(sorted(candidates),target,0,[],res)
        return res
    def DFS(self, nums,target,idx,path,res):
        if target == 0 : 
            res.append(path)
        elif target < 0 :
            return
        for i in range(idx,len(nums)):
            #중복 처리
            if i > idx and nums[i] == nums[i-1]:
                continue
            self.DFS(nums,target-nums[i],i+1,path + [nums[i]],res)

'''
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()                      
        result = []

        def combine_sum_2(nums, start, path, result, target):
            if not target:
                result.append(path)
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                if nums[i] > target:
                    break

                combine_sum_2(nums, i + 1, path + [nums[i]], result, target - nums[i])

        combine_sum_2(candidates, 0, [], result, target)
        return result
'''
candidates = [10,1,2,7,6,1,5]
target = 8
test = Solution()
print(test.combinationSum2(candidates, target))