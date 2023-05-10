from typing import List
from itertools import combinations_with_replacement

''' 재귀로 풀기 (백트랙킹) '''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(sum_candi, idx, path): # dfs(남아있는 수, 반복할 인덱스, 여태까지 배열)
            if sum_candi < 0: # 인덱스를 순회하면서 target에서 빼줄텐데 뺀 수가 음수가 되면 걍 리턴
                return
            if sum_candi == 0: # 0이 되면 해당 리스트 추가
                ret.append(path[:])
                return
            for i in range(idx, len(candidates)): # idx 부터 반복문 돌면서 단계별 dfs 시작
                dfs(sum_candi - candidates[i], i , path + [candidates[i]])
        ret = []
        dfs(target, 0, [])
        return ret

''' 반복문으로 풀기
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cache = [[] for _ in range(target + 1)]
        cache[0] = [[]]
        for c in candidates:
            for i in range(target + 1):
                if i >= c:
                    for temp_ans in cache[i - c]:
                        cache[i].append(temp_ans + [c])
        return cache[-1]
'''

candidates = [2,3,6,7]
target = 7
test = Solution()
print(test.combinationSum(candidates, target))