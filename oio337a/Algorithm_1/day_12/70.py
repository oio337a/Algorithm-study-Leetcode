'''
        1 2 3 4 5
        1 2 3 5 8

        1,1,1  1
        1,2    1
        2,1    1

        1,1,1,1 /
        1,2,1 /
        1,1,2
        2,1,1 /
        2,2 
      
        f(n) = f(n-1) + f(n-2)
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2] # dp 테이블 생성 (초기값 셋팅)

        if n < 3: # dp 테이블 크기보다 n이 작을 때 (1, 2인 경우)
            return dp[n]
        for i in range(3, n+1): # dp 테이블 갱신 n까지
            num = dp[i - 1] + dp[i - 2]  # 점화식 f(n) = f(n-1) + f(n-2)
            dp.append(num) # 해당 수 dp 테이블에 추가
        return dp[n]


n = 3
test = Solution()
print(test.climbStairs(n))
