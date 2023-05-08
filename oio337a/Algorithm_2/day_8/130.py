from typing import List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0]) # row, col 세팅
        v = [[0]*col for _ in range(row)] # visited 2차원 배열
        queue = deque()
        dx = [-1,0,1,0] # 방향 벡터 생성
        dy = [0,-1,0,1]

        # 가장자리에 '0'이 있으면 q 에 삽입
        for i in range (col) :
            if board[0][i] == 'O': 
                queue.append([0,i])
            if board[row-1][i] =='O':
                queue.append([row-1,i])
        for i in range (row):
            if board[i][0] == 'O' :
                queue.append([i,0])
            if board[i][col-1] =='O':
                queue.append([i,col-1])

        while queue :
            x, y = queue.popleft()
            v[x][y] = 1 # 방문 체크
            for i in range(4) :
                nx, ny = x + dx[i], y + dy[i] # 4방 탐색
                # 보드에 있고, 방문 안했고, '0'일때
                if 0 <= nx < row and 0 <= ny < col and v[nx][ny] == 0 and board[nx][ny] == 'O':
                    v[nx][ny] = 1 # 방문체크
                    queue.append([nx,ny])

        # board 돌면서 visited == 0일때 'X' 아닐때 '0'
        for i in range(row) : 
            for j in range(col):
                if v[i][j] == 0 :
                    board[i][j] = 'X'
                else :
                    board[i][j] = 'O'
        return board 

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
test = Solution()
test.solve(board)
print(board)