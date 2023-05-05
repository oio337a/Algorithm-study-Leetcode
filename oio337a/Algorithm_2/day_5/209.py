from typing import List


# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         s, e = 0, 0
#         hap = nums[0]
#         l = len(nums)
#         found = False

#         if l == 0:
#             return 0
#         while s <= e and e < len(nums):
#             if hap < target:
#                 e += 1
#                 if e < len(nums):
#                     hap += nums[e]
#             elif hap >= target:
#                 if l >= e - s + 1:
#                     l = e - s + 1
#                     found = True
#                 if hap > target:
#                     hap -= nums[s]
#                     s += 1
#                 else:
#                     e += 1
#                     if e < len(nums):
#                         hap += nums[e]
#         if found:
#             return l
#         return 0

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l, r = 0, len(nums)+1
        sub = 0
        for i in range(len(nums)):
            sub += nums[i]
            while sub >= s:
                r = min(r, i-l+1)
                sub -= nums[l]
                l += 1
        return r if r != len(nums) + 1 else 0


target = 7
nums = [2,3,1,2,4,3]
test = Solution()
print(test.minSubArrayLen(target, nums))