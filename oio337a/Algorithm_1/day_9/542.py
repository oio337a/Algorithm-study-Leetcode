from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m , n = len(mat), len(mat[0]) # 행, 열 길이구하기
        dx = [0, 0, -1, 1] # 좌표 생성
        dy = [1, -1, 0, 0]
        q = deque() # 큐생성
        for i in range(m): # 맵 루프 돌기
            for j in range(n):
                if mat[i][j] == 0: # 0이면 큐에 추가
                    q.append((i, j))
                else: # 아니면 10의 9승 (엄청 큰 수)으로 변환
                    mat[i][j] = 1e9
        while q:
            x, y = q.popleft() # 요소 추출 0 좌표
            for k in range(4): # 4방 탐색
                nx = x + dx[k]
                ny = y + dy[k]
                z = mat[x][y] + 1 # 현재 값 + 1 (0 -> 1 -> 2)
                if 0 <= nx and nx < m and 0 <= ny and ny < n and mat[nx][ny] > z:
                    mat[nx][ny] = z
                    q.append((nx,ny))
        return (mat)

solution = Solution()
mattt = [[0,0,0],[0,1,0],[1,1,1]]
for i in mattt:
    print(*i)
solution.updateMatrix(mattt)
print()
for i in mattt:
    print(*i)
print()
answer = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]]
for i in answer:
    print(*i)


''' 
    time out code 
    1을 기준으로 코드를 작성하니 타임오버가 떠버렷다.....
    블로그 참조하니 0을 기준으로 하더라구요.
    세상에 똑똑한 사람 참 많어~!!
'''
# from typing import List


# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         m = len(mat)
#         n = len(mat[0])
#         start = 1
#         flag = 0
#         d_4 = [-1, 1, -1, 1]
#         while start:
#             for i in range(m):
#                 for j in range(n):
#                     top = i + d_4[0]
#                     bottom = i + d_4[1]
#                     left = j + d_4[2]
#                     right = j + d_4[3]
#                     if top < 0:
#                         top = i
#                     if bottom >= m:
#                         bottom = i
#                     if left < 0:
#                         left = j
#                     if right >= n:
#                         right = j
#                     print(f"i: {i}, j:{j}, l:{left}, r:{right}, t:{top}, b:{bottom}")
#                     if mat[i][left] >= start and mat[i][right] >= start and mat[top][j] >= start and mat[bottom][j] >= start and mat[i][j] == start:
#                         mat[i][j] += 1
#                         flag = 1
#             if flag:
#                 start += 1
#                 flag = 0
#             else:
#                 start = 0
#         return (mat)

# solution = Solution()
# mattt = [[0],[1]]
# for i in mattt:
#     print(*i)
# solution.updateMatrix(mattt)
# print()
# for i in mattt:
#     print(*i)
# print()
# answer = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]]
# for i in answer:
#     print(*i)