from typing import List

def letterCasePermutation(s: str) -> List[str]:
    def backtrack(start, permu_s):
        if len(permu_s) == len(s):
            res.append(permu_s[:])
            return 
        
        for i in range(start, len(s)):
            if s[i].isdigit():
                backtrack(i + 1, permu_s + s[i])
            else :
                lower_result = permu_s + s[i].lower()
                backtrack(i + 1, lower_result)
                upper_result = permu_s + s[i].upper()
                backtrack(i + 1, upper_result)

    res = []
    backtrack(0, "")
    return res
print("res=", letterCasePermutation("a1b2"))