from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      cnt = 0 # 반환할 갯수
      m, n = len(grid[0]), len(grid) # r, c 길이 측정
      dx = [0, 0, 1, -1] # 방향 좌표 생성
      dy = [1, -1, 0, 0]
      q = deque() # que 생성
      for i in range(n):
         for j in range(m): # 맵 전체 탐색
            if grid[i][j] == '1': # 1인 지점 찾기
               q.append((i, j)) # que 에 추가
               cnt += 1 # 시작이니 땅 갯수 ++
               while q: # 해당 좌표부터 bfs 시작
                  x, y = q.popleft() # 첫번쨰 값 꺼내서
                  grid[x][y] = 0 # 해당 땅 0으로 visited 체크
                  for k in range(4): # 4방 탐색
                     nx = x + dx[k]
                     ny = y + dy[k]
                     if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '1' and (nx, ny) not in q: # 범위안에 잇고 1일때
                        q.append((nx, ny)) # 큐에 탐색할 값 추가
      return cnt


grid = [["1", "0"]]
test = Solution()
print(test.numIslands(grid))
