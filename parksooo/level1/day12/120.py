from typing import List
import sys
def minimumTotal(triangle: List[List[int]]) -> int:
    if len(triangle) == 1:
        return triangle[0][0]
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    res = sys.maxsize #인트형 맥스
    for i in range(1, n):
        for j in range (0, i + 1): # i + 1 만큼 정해주어서 [i][j]의 범위를 다 확인한다
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = min(dp[i- 1][j], dp[i - 1][j - 1]) + triangle[i][j]
            if i == n - 1:
                res = min(res, dp[i][j])
    return res

print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))