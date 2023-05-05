from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ct_p = Counter(p) # p str에 대한 정보를 알려주는 카운터 사용
        res = []
        limit = len(s) - len(p) + 1 # p 길이 만큼 s에서 비교하는 것이기에 효율을 높임
        l_p = len(p)
        for i in range(limit):
            if Counter(s[i : i + l_p]) == ct_p: # substr 한 카운터를 p 카운터와 비교
                res.append(i)
        return res

test = Solution()
print(test.findAnagrams("cbaebabacd", "abc"))
print(test.findAnagrams("abab", "ab"))