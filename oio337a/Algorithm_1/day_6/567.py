# Counter 객체
# s = "hello" 일 때 
# Counter(s)
# 하게 되면 Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1}) 반환
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1) # s1 길이 저장
        temp_1 = Counter(s1) # s1 counter 객체 변환
        for start in range(0, len(s2) - s1_len + 1): # 처음부터 전체 길이에 s1길이 만큼 뺀 곳까지 반복
            temp_2 = Counter(s2[start:start + s1_len]) # s2, start 부터 s1 길이 만큼 counter 변환
            if len(temp_2 - temp_1) == 0: # 0 이라면 s1 == s2 임
                return (1)
        return (0)
