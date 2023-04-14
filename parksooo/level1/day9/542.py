from typing import List
from collections import deque

def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    dq = deque()
    row, col  = len(mat), len(mat[0])
    dx = [1, 0, -1, 0] 
    dy = [0, 1, 0, -1] #bfs 사용하기 위해서 4방향 서치를 위한 것
    for i in range(row):
        for j in range(col):
            if mat[i][j] == 0:
                dq.append((i, j)) # 0일때 append
            else :
                mat[i][j] = 2147483647 # 0이외의 값은 최대값으로 설정 왜냐면 길이를 재야하기에 
    while dq:
        x, y = dq.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            z = mat[x][y] + 1 #길이이기에 1을 더해준다 
            if 0 <= nx < row and 0 <= ny < col and mat[nx][ny] > z:
                mat[nx][ny] = z # 0부터의 길이이기에 z값을 넣어줌
                dq.append((nx, ny)) # 다시 탐색
    return mat
            
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(updateMatrix(mat))