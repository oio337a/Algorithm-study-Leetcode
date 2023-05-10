from typing import List
from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        dq = deque([(0,[])]) # 덱에 0번째 노드인지 알려주는 숫자와, [] 배열을 같이 넣어준다
        while dq:
            node, path = dq.popleft() # pop 해서 node는 길이 - 1 에서 결과값에 넣어준다. path는 갈수 있는 길이다.
            if node == len(graph) - 1:
                res.append(path + [node])
            for i in graph[node]: # 각 노드에서 갈수 있는 길을 다 append 해준다
                dq.append([i, path + [node]])
        return res
test = Solution()
print(test.allPathsSourceTarget([[1,2],[3],[3],[]]))