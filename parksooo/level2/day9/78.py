from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sub = [], []
        def dfs(id):
            if id == len(nums):
                res.append(sub[:])
                return
            sub.append(nums[id])
            dfs(id + 1) # [1] [1 2] [1 2 3] 순으로 먼저 확인을 한다
            sub.pop()
            dfs(id + 1) # 그후에 뒤에서 부터 하나씩 pop 하면서 재귀를 돈다
        dfs(0)
        return res

test = Solution()
print(test.subsets([1,2,3]))