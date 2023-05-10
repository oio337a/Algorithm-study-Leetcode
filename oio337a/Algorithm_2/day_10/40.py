from typing import List
from itertools import combinations

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, t, idx, path, res):
            if t == 0:
                res.append(path)
            elif t < 0:
                return
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]: # 인덱스가 증가하지 않았거나, nums 의 값이 전값과 같다면 스킵
                    continue
            dfs(nums, target - nums[i], i + 1, path + [nums[i]], res)
        res = []
        dfs(sorted(candidates), target, 0, [], res)
        return res

candidates = [10,1,2,7,6,1,5]
target = 8
test = Solution()
print(test.combinationSum2(candidates, target))