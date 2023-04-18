from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for key, val in Counter(nums).items(): # Counter 변환 후 key 와 value 로 순회
            if val == 1: # value 값이 1 == key 값 출력
                return key

nums = [4,1,2,1,2]
test = Solution()
print(test.singleNumber(nums))