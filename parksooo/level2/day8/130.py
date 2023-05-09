from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        visited = [[0 for i in range(n)] for j in range(m)]
        direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dq = deque()
        for i in range(n):
            if board[0][i] == 'O':
                dq.append((0, i))
            if board[m - 1][i] == 'O':
                dq.append((m - 1, i))
        for j in range(m):
            if board[j][0] == 'O':
                dq.append((j, 0))
            if board[j][n - 1] == 'O':
                dq.append((j, n - 1))
        # 위에 부분은 경계선에 걸쳐있는 O 친구들을 덱에 넣어준다
        while dq: # 경계선에 있는 친구들과 경계에 있는 친구들을 visted로 만들어준다
            col, row = dq.popleft()
            visited[col][row] = 1 # 방문 한것이라고 표시한다 그렇다면 다 경계에 있는 O이기 떄문
            for x, y in direct:
                ny, nx = col + y, row + x
                if 0 <= ny < m and 0 <= nx < n and board[ny][nx] == 'O' and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    dq.append((ny, nx))
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0: # 방문하지 않은 곳은 X로 만들어준다
                    board[i][j] = 'X'
        print(board)
test = Solution()
a = [["O","O"],["O","O"]]
a1 =[["X","X","X"],["X","O","X"],["X","X","X"]]
# print(test.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
test.solve(a1)