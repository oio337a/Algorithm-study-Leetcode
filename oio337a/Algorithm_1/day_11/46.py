from typing import List
from itertools import permutations as p


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return (list(p(nums, len(nums))))
        # 순열 모듈 사용


nums = [1, 2, 3]
test = Solution()
print(test.permute(nums))
