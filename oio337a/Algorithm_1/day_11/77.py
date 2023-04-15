from typing import List
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return (list(combinations(range(1, n + 1), k)))
        # 조합 모듈 사용


n = 4
k = 2
test = Solution()
test.combine(n, k)
