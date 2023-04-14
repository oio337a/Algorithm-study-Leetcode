from collections import deque
from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    dq = deque() # bfs 사용
    row, col = len(grid), len(grid[0])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[0] * col for _ in range(row)]
    cnt = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 2:
                dq.append((i, j, cnt)) # 이번에는 append 할때 횟수를 같이 함
    
    while dq:
        x, y, cnt = dq.popleft()
        visited[x][y] = 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 1 and not visited[nx][ny]:
                grid[nx][ny] = 2
                dq.append((nx, ny, cnt + 1)) # 횟수를 더해서 얼마나 시간이 걸리는 지 확인
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                return -1 # 1 있으면 fresh한 놈이 있으니 리턴 
    return cnt

# grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[0,2]]
print(orangesRotting(grid))