from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        counting = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(1,nums[i]+1):
                if i + j >= len(nums):
                    continue
                if counting[i+j] == 0 :
                    counting[i+j] = counting[i]+1
        return counting[len(nums)-1]

''' 2진탐색 풀이 방법
import bisect
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            return 1

        steps = [len(nums) - 1]

        for i in range(len(nums) - 2, -1, -1):
            current_node = nums[i]
            step = i + current_node
            idx = bisect.bisect_right(steps, step)

            if idx > 0:
                steps = steps[idx - 1:]
                steps.insert(0, i)
            else:
                steps.insert(0, step)

        return len(steps) - 1


if __name__ == '__main__':
    print(Solution().jump([1,2,1,1,1]))

'''
nums = [2,3,0,1,4]
test = Solution()
print(test.jump(nums))
