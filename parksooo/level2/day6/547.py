from typing import List
from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        cnt = 0
        visited = [0 for i in range(n)]
        for i in range(n):
            if visited[i] == 0:
                cnt += 1
                dq = deque()
                dq.append(i)
                visited[i] = 1
                while dq:
                    x = dq.popleft()
                    for j in range(n):
                        if visited[j] == 0 and isConnected[x][j] == 1:
                            visited[j] = 1
                            dq.append(j)
        return cnt

test = Solution()
b = [[1,1,0],
     [1,1,0],
     [0,0,1]]
print(test.findCircleNum(b))