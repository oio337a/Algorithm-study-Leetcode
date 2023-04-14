from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0 # 반환 할 시간 변수
        row = len(grid) # 행 열 길이 구하기
        col = len(grid[0])
        dx = [0, 0, -1, 1] # 방향 벡터 설정
        dy = [1, -1, 0, 0]
        visited = [[0] * col for _ in range(row)] # 방문 여부 2차원 배열
        q = deque() # 큐생성
        for i in range(row): # 맵 돌면서 썩은 오렌지 찾기
            for j in range(col):
                if grid[i][j] == 2: # 찾으면 시간이랑 함께 어펜드
                    q.append((i, j, time))
        while q: # 탐색 할 좌표가 있을 때까지 반복
            x, y, time = q.popleft() # 값 추출 (1인 오렌지)
            visited[x][y] = 1 # 방문 체크
            for i in range(4): # 4방 탐색
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx and nx < row and 0 <= ny and ny < col and not visited[nx][ny]: # 보드 안에있고, 방문 X
                    if grid[nx][ny] == 1: # 4방향 중 다음 좌표가 싱싱한 오렌지라면
                        grid[nx][ny] = 2 # 썩히고
                        q.append((nx, ny, time + 1)) # 좌표 append time + 1
        for i in range(row): # 맵 돌면서 싱싱한게 있는지 체크
            for j in range(col):
                if grid[i][j] == 1:
                    return -1 # 있다면 -1 리턴
        return time

case = [[2,1,1],[1,1,0],[0,1,1]]

test = Solution()
test.orangesRotting(case)