from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 0
        curr = 0
        jmp_cnt = 0
        jmps = 0
        for i in range(l - 1):
            jmp_cnt = max(nums[i] + i, jmp_cnt)
            if i == curr:
                jmps += 1
                curr = jmp_cnt    
        return jmps

test = Solution()
print(test.jump([1,2,1,1,1,1]))
print(test.jump([1, 2, 1, 1, 1]))
print(test.jump([1, 2]))
