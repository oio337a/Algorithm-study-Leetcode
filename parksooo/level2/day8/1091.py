from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        direct1 = [(-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)]

        dq = deque()
        dq.append((0, 0, 1)) # 0,0 부터 시작하기때문에 굳이 for문을 돌릴필요가 없음
        while dq:
            row, col, cnt = dq.popleft()
            if row == n - 1 and col == n - 1:
                return cnt
            for x, y in direct1:
                nx, ny = row + x, col + y
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    dq.append((nx, ny, cnt + 1))
        return -1

test = Solution()
a = [[0,1,1,1,1,1,1,1],[0,1,1,0,0,0,0,0],[0,1,0,1,1,1,1,0],[0,1,0,1,1,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,0,1,0],[0,0,0,0,0,1,1,0],[1,1,1,1,1,1,1,0]]
print(test.shortestPathBinaryMatrix(a))
