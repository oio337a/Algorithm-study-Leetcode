from typing import List

# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         def backTracking(sub, id):
#             if sum(sub) == target:
#                 sub.sort()
#                 if list(sub) not in res:
#                     res.append(list(sub))
#                 return
#             if sum(sub) > target:
#                 return
#             for n in range(id, len(candidates)):
#                 sub.append(candidates[n])
#                 backTracking(sub, n + 1)
#                 sub.pop()
#         backTracking([], 0)
#         return res
# 이 방법은 시간 초과가 떴다. 그 이유는 아마 모든 요소를 다 재귀를 돌렸기 때문이지 않을까 싶어서 코드를 바꾸어보았다
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backTracking(sub, id):
            if sum(sub) == target:
                res.append(list(sub))
                return
            if sum(sub) > target:
                return
            for n in range(id, len(candidates)):
                if n > id and candidates[n] == candidates[n - 1]:
                    continue
                backTracking(sub + [candidates[n]], n + 1)
        backTracking([], 0)
        return res
# 이 방식은 candidates의 값이 중복될 경우 스킵했기에, sort하거나 이런 일을 하지 않아도 되어서 더 빠르다
test = Solution()
print(test.combinationSum2([10,1,2,7,6,1,5], 8))
print(test.combinationSum2([2,5,2,1,2], 5))
