from collections import Counter

class Solution:
	def hammingWeight(self, n: int) -> int:
		count = 0
		while n:
			n &= n - 1 # 비트 연산을 n에 적용하는 것
			count += 1 # 계산 수 만큼 count
		return count

test = Solution()
n = 0b11111111111111111111111111111101
print(test.hammingWeight(n))
