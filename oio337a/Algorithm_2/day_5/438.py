from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
      # s 와 p 길이 구하기
      s_len = len(s)
      p_len = len(p)
      # counter 변환
      count = Counter(p)
      result = []
      
      for i in range(s_len - p_len + 1): # p 길이 뺸 것 까지 범위
         if Counter(s[i:i+p_len]) == count: # counter 변환 후 비교
            result.append(i) # 같으면 인덱스 추가
      return result
         

s = "cbaebabacd"
p = "abc"

test = Solution()
print(test.findAnagrams(s, p))