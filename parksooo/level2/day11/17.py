from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {"2" : "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        #딕셔너리 하나를 만들어서 판별한다
        res = []
        def dfs(str, d_next):
            if not d_next: #하나씩 슬라이딩을 하면서 만든 digits이 null이면 리턴
                res.append(str)
                return
            for l in phone[d_next[0]]: # 2에 대한 str의 첫번쨰를 넣고, 3에 해당하는 str을 가지고 판단
                dfs(str + l, d_next[1:])
        dfs("", digits)
        return res

test = Solution()
print(test.letterCombinations("23"))