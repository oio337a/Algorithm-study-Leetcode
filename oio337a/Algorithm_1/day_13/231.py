class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 2 == 0:
                n /= 2
            else:
                return False
        return True

n = 1
test = Solution()
print(test.isPowerOfTwo(n))