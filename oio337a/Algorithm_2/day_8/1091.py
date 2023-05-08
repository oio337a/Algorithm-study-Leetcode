from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]: # 시작, 끝이 1이면 -1리턴
            return -1
        cnt = 1 # 반환할 cnt 값 생성
        dx = [1, 1, 1, 0, 0, -1, -1, -1] # 방향 벡터 셋팅
        dy = [1, 0, -1, 1, -1, 1, 0, -1]
        n = len(grid) # grid 크기 셋팅
        visited = [[0]*n for _ in range(n)] # 방문 확인 2차원 배열 생성
        q = deque()
        q.append((0, 0, cnt)) # 첫번째 좌표 생성
        while q: # q 다돌 때까지 반복
            x, y, cnt = q.popleft() # x, y, cnt 꺼내기
            if x == n - 1 and y == n - 1: # 종료 조건 (끝값)
                return cnt
            for i in range(8): # 8방 탐색
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                    visited[nx][ny] = 1 # 방문 체크
                    q.append((nx, ny, cnt + 1)) # 탐색할 좌표 추가
        return -1

grid = [[0,0,0],[1,1,0],[1,1,0]]
test = Solution()
print(test.shortestPathBinaryMatrix(grid))