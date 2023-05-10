from collections import Counter
from itertools import combinations
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backTracking(sub, id): # 값이 타겟과 같을 때 넣어줍니다
            if sum(sub) == target:
                res.append(list(sub))
                return
            if sum(sub) > target: # 커지면 함수를 종료 시켜 버립니다
                return
            for n in range(id, len(candidates)): # 하나 넣고 백트래킹돌리고 팝해서 다음 인덱스의 값을 넣어줍니다!
                sub.append(candidates[n])
                backTracking(sub, n)
                sub.pop()
        backTracking([], 0)
        return res


test = Solution()
print(test.combinationSum([2, 3, 5], 8))