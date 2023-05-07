from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set() # 방문 여부 체크 set 세팅

        def dfs(isConnected, visited, i): # dfs함수 
            if i in visited: # 방문한 노드면 0리턴
                return 0
            visited.add(i) # 방문하지 않았음 -> 값 추가
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1: # 반복문 돌면서 해당 노드 확인
                    dfs(isConnected, visited, j)
            return 1 # 노드들 추가했으면 1리턴
        provinces = 0
        for i in range(len(isConnected)):
            provinces += dfs(isConnected, visited, i)
        return provinces


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
test = Solution()
print(test.findCircleNum(isConnected))
