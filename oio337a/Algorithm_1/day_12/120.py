from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        for i in range(1, m):
            triangle[i][0] += triangle[i-1][0] # 왼쪽은 왼쪽 숫자 싹 더해버리기
            triangle[i][-1] += triangle[i-1][-1] # 오른쪽은 오른쪽
        for i in range(2, m): # 2번째 줄 부터 시작
            for j in range(1, i): # 1번째 인덱스 부터 i 까지
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j]) # 왼 오 중 최소 더하기
        print(triangle)
        return min(triangle[-1]) # 마지막 줄 최소값 출력


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
test = Solution()
print(test.minimumTotal(triangle))
