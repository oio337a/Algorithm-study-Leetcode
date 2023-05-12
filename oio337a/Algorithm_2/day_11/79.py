from typing import List
from collections import deque

''' bfs 했다가 실패 함. bfs 로 풀면 안댐...
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[0] * n for _ in range(m)]
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        q = deque()
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    q.append((i, j, 1))
                    while q:
                        x, y, idx = q.popleft()
                        visited[x][y] = 1
                        if idx == len(word):
                            return True
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == word[idx] and not visited[nx][ny]:
                                q.append((nx, ny, idx + 1))
                visited = [[0] * n for _ in range(m)]
        return False
'''

class Solution:
    def exist(self, board, word: str) -> bool:
        R, C = len(board), len(board[0])

        def dfs(row, col, word):
            if not word:
                return True
            origin = board[row][col]
            board[row][col] = '#'
            for r, c in (
                    (row+1, col), (row-1, col),
                    (row, col+1), (row, col-1)):
                if (0 <= r < R and 0 <= c < C and
                        board[r][c] == word[0] and dfs(r, c, word[1:])):
                    return True
            board[row][col] = origin

        for row in range(R):
            for col in range(C):
                if (board[row][col] == word[0] and
                        dfs(row, col, word[1:])):
                    return True
        return False

board =[["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"]]
word = "ABCESEEEFS"
test = Solution()
print(test.exist(board, word))