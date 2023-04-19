from typing import List

class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		res = 0
		for i in range(len(nums)):
			res = res^nums[i] # ^ 같으면 0 다르면 1 을 반환하는 특성을 사용함! 
		return res

test = Solution()
print(test.singleNumber([1, 2, 3, 1, 2]))