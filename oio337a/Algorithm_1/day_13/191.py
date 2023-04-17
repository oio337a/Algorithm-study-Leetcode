class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n >= 1: # 2진수에서 1이 나오는 경우는 홀수 인 경우
            if n % 2 == 0: # 2로 나눠 지면 걍 나누기
                n /= 2
            else: # 2로 안나눠 지면 cnt += 1 n - 1
                cnt += 1
                n -= 1
        return cnt

n = 0b11111111111111111111111111111101
test = Solution()
print(test.hammingWeight(n))