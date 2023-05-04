from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if firstList == [] or secondList == []:
            return []
        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            a = max(firstList[i][0], secondList[j][0]) # 맥스값을 찾는다
            b = min(firstList[i][1], secondList[j][1]) # 미니값을 찾는다
            if a <= b: # 인터벌이 적용되는 구간
                res.append([a, b])
            if firstList[i][1] < secondList[j][1]: # 값이 겹치는 곳을 확인하기 위해서 
                i += 1 # 작은 곳을 옮긴다
            else :
                j += 1 
        return res

test = Solution()
print(test.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))