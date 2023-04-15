from typing import List

'''
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = [""]
        for i in range(len(s)):
            temp = []
            for j in range(len(answer)):
                if s[i].isalpha():
                    temp.append(answer[j] + s[i].lower())
                    temp.append(answer[j] + s[i].upper())
                else:
                    temp.append(answer[j] + s[i])
            answer = temp
        return answer
'''

# 개천재다...
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = ['']
        for c in s:
            if c.isalpha():
                res = [i + j for i in res for j in [c.upper(), c.lower()]]
            else:
                res = [i + c for i in res]
            print(res)
        return res

s = "a1b2"
test = Solution()
print(test.letterCasePermutation(s))
