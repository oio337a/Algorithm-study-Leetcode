from collections import Counter
from typing import List
from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        per = list(permutations(nums))
        res = []
        for i in (per):
            if i not in res:
                res.append(i)
        return res
# 제가 푼 방식은 내장함수를 사용하여 순열을 만들어서 중복 없이 append해서 넣어 준다
# 하지만 시간이 너무 오래걸림  
class Solution1:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(sub, counter):
            if len(sub) == len(nums):
                res.append(list(sub))
                return
            for n in counter:
                if counter[n] > 0:
                    sub.append(n)
                    counter[n] -= 1
                    dfs(sub, counter)
                    sub.pop()
                    counter[n] += 1
        dfs([], Counter(nums))
        return res
# 참조한 방식 : 백트래킹을 사용한다
# 카운터를 사용하여, nums의 길이만큼 sub이라는 [] 에 추가 되면, 그것을 res에 넣어준다. 
# 중복은 sub.pop을 통해서 삭제해준다


test = Solution1()
print(test.permuteUnique([1,1,2]))