from typing import List
from functools import reduce

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         def multiply(arr):
#             return reduce(lambda x, y: x * y, arr)
#         res = 0
#         l_n = len(nums)
#         for i in range(l_n):
#             j = 1
#             while j + i <= l_n:
#                 print(nums[i : i + j], i , j)
#                 if multiply(nums[i : i + j]) >= k:
#                     break
#                 else :
#                     res += 1
#                 j += 1
#         return res 시간 초과로 털러벼림;;

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        j, res = 0, 0
        mul, l_n = 1, len(nums)

        for i in range(l_n):
            mul *= nums[i]
            while mul >= k: # 클때 까지만 나누어서 j 인덱스를 i 인덱스에서 뺴서 갯수를 더해준다. 
                mul /= nums[j]
                j += 1
            res += i - j + 1
        return res
    
test = Solution()
print(test.numSubarrayProductLessThanK([10,5,2,6], 100))
print(test.numSubarrayProductLessThanK([1,2,3], 0))


