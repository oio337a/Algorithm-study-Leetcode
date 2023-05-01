from typing import List

class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j] == target:
					return True
		return False

class Solution2:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		m = len(matrix)
		n = len(matrix[0])
		s = 0
		e = (m * n) - 1
		while s <= e:
			mid = s + (e - s) // 2
			r = mid // n
			l = mid % n
			if matrix[r][l] == target:
				return True
			elif matrix[r][l] > target:
				e = mid - 1
			else : 
				s = mid + 1
		return False

test = Solution()
test2 = Solution2()
print(test2.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))