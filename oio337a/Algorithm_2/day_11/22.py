from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(idx, ans, k, p):
            if len(ans) == n * 2:
                result.append(ans)
                return
            for i in range(idx, n * 2):
                for j in range(2):
                    if j == 0:
                        if k == n:
                            continue
                        dfs(i + 1, ans + letters[0], k + 1, p)
                    else:
                        if p == k:
                            continue
                        dfs(i + 1, ans + letters[1], k, p + 1)

        result = []
        letters = ["(", ")"]
        dfs(0, "", 0, 0)
        return result

''' 반복문 없이 재귀 
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def helper(openN, closedN):
            if openN==closedN==n:
                res.append(''.join(stack))
                return
            
            if openN<n:
                stack.append('(')
                helper(openN+1,closedN)
                stack.pop()
            if closedN<openN:
                stack.append(')')
                helper(openN, closedN+1)
                stack.pop()
        helper(0,0)
        return res
'''

n = 3
test = Solution()
print(test.generateParenthesis(n))