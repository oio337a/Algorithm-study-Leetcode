class Solution:
	def isPowerOfTwo(self, n: int) -> bool:
		power = 0
		while True:
			if 2 ** power == n:
				return True
			if 2 ** power > n:
				return False
			power += 1

# class Solution2:
# 	def ispowerOfTwo(self, n : int) -> bool:
# 		if n == 0:
# 			return False
# 		return n == 1 or (n % 2 == 0 and self.ispowerOfTwo(n // 2))
# 재귀로는 이렇게 풀면 되네요!
test = Solution()
print(test.isPowerOfTwo(3))