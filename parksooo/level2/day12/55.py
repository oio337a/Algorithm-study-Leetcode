from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        # dp = [0 for i in range(l)]
        jmp_cnt = 0
        for i in range(l):
            if jmp_cnt < i: # 현지점을 갈수 있는지 판단하는 경우
                return False
            jmp_cnt = max(nums[i] + i, jmp_cnt)
        return True

test = Solution()
a = [1, 3, 2, 1, 1, 1, 1]
print(test.canJump(a))
