from typing import List
from collections import deque

def maxAreaOfIsland(grid: List[List[int]]) -> int:
	max_size = 0
	size = 0
	row, col = len(grid), len(grid[0])
	for i in range(row): # 전체 순회하면서 섬인 부분일 경우 덱에 넣어서 4방향을 판단
		for j in range(col):
			if grid[i][j] == 1:
				size = 0
				queue = deque()
				queue.append((i, j))
				
				while queue: # 덱의 요소가 없어질 때까지 size를 구한다
					x, y = queue.popleft()
					grid[x][y] = 0 # 방문을 했기에 0으로 만들어준다
					size += 1

					for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
						if 0 <= i < row and 0 <= j < col and grid[i][j] == 1:
							queue.append((i, j))
							grid[i][j] = 0 # 중복 방문을 막기위해서 0으로 만든다
			max_size = max(max_size, size) # max 값을 찾아서
	
	return max_size
