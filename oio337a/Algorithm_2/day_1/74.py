from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s, e = 0, len(matrix) - 1
        if e == 0: # 행이 1개 일 때
            mid = 0
        else:
            while s <= e: # 인덱스 0 번째를 보고 target이 속하는 행 찾기
                mid = (s + e) // 2
                if mid == len(matrix) - 1:
                    break
                if matrix[mid][0] <= target and matrix[mid + 1][0] > target:
                    break
                if matrix[mid][0] < target:
                    s = mid + 1
                else:
                    e = mid - 1
        for i in matrix[mid]: # target 이 속하는 행 순환 탐색
            if i == target:
                return True
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
test = Solution()
print(test.searchMatrix(matrix, target))
