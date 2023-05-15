from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = []
        m, n, w = len(board), len(board[0]), len(word)
        visited = [[0 for i in range(n)] for j in range(m)]
        def dfs(y, x, id):
            if w == id:
                return True
            if x < 0 or y < 0 or x >= n or y >= m:
                return False
            if word[id] != board[y][x]:
                return False
            if visited[y][x]: # 방문했기에 false를 준다
                return False
            visited[y][x] = True # 방문했다고 체크한다
            res = dfs(y - 1, x, id + 1) or dfs(y + 1, x, id + 1) or dfs(y, x - 1, id + 1) or dfs(y, x + 1, id + 1)
            # 4 방향을 dfs를 돌린다 그래서 스텍을 다 쌓아서 return이  true 가 되면 알맞은 word를 찾은 것이다
            visited[y][x] = False # 다시 돌려놓는다
            return res
        for i in range(m):
            for j in range(n):
                if (dfs(i, j, 0)):
                    return True
        return False


test = Solution()
print(test.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))