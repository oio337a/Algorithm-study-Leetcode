from typing import List
from itertools import combinations

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        l = len(digits)
        temp = []
        for i in digits:
            temp.append(list(letters[i]))
        
        return 0


digits = "23"
test = Solution()
print(test.letterCombinations(digits))