from typing import List

class Solution1:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, sub = set(), [] # set 자료 형을 사용해서 중복을 제거 해준다 앞선 70번과 같은 로직이지만, 중복임을 체크하는 것이 있다
        nums.sort()
        def dfs(id):
            if id == len(nums):
                if tuple(sub) not in res: # set과 배열을 비교할수 없으니, tuple이라는 자료형을 사용하여 비교한다
                    res.add(tuple(sub)) # 없으면 넣어준다 있으면 안넣음!
                return
            sub.append(nums[id]) # append pop 은 똑같다
            dfs(id + 1)
            sub.pop()
            dfs(id + 1)
        dfs(0)
        return res


test = Solution1()
print(test.subsetsWithDup([1,2,2]))