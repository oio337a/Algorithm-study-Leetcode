from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(combi_str, left, right):
            if len(combi_str) == 2 * n:
                res.append("".join(combi_str))
                return
            if left < n :
                combi_str.append("(")
                dfs(combi_str, left + 1, right)
                combi_str.pop()
            if left > right :
                combi_str.append(")")
                dfs(combi_str, left, right + 1)
                combi_str.pop()
        dfs([], 0, 0)
        return res
test = Solution()
print(test.generateParenthesis(2))