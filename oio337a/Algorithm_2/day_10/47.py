from typing import List
from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set(permutations(nums, len(nums)))) # 모듈 사용하여 풀이


nums = [1,1,2]
test = Solution()
print(test.permuteUnique(nums))