from typing import List

class Solution:
    def __init__(self):
        self.paths = []
        self.graph = {}
        
    # dict 형태로 graph 를 만든다
    # {0: [1,2,3], 1:[2,3,], ...} 이런 식으로
    def buildGraph(self, graph):
        for i, neighbors in enumerate(graph):
            self.graph[i] = neighbors

    # src == dest 일 때 까지 재귀 호출하고 path에 그 경로 누적 
    # src == dest 인 순간 누적한 경로를 결과값에 추가한다.
    def setPaths(self, src, dest, path):
        if src == dest:
            self.paths.append(path)
            return
        
        # 경로탐색 재귀호출
        for neighbor in self.graph[src]:
            self.setPaths(neighbor, dest, path + [neighbor])
                          
            
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # 일단 input을 dict 형태로 만듦
        self.buildGraph(graph)
        # 0 부터 size-1 (인덱스 0부터 시작이니까..) 까지 탐색
        self.setPaths(0, len(graph)-1, [0])
        
        return self.paths

graph = [[1,2],[3],[3],[]]
test = Solution()
print(test.allPathsSourceTarget(graph))