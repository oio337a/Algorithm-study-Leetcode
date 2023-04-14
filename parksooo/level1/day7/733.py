from collections import deque
from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
	pos_color = image[sr][sc] # 현재 위치의 색을 저장한다 왜냐? 현재 색갈과 같은 곳만 new color로 바꾸어야하기에
	row, col = len(image), len(image[0]) # 범위 설정을 위한 길이 설정

	if pos_color != color: # 칠하려는 색갈과 지금 위치의 색이 다르다면 덱을 만들어서 추가한다
		queue = deque()
		queue.append((sr, sc))

		while queue : # 추가한 큐를 가지고 4방향을 방문하면서 같은 색이라면 다시금 큐에 추가하면서 새로운 색으로 칠해준다
			x, y = queue.popleft()
			image[x][y] = color

			for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)): # 파이썬은 편하구나;;
				if 0 <= i < row and 0 <= j < col and image[i][j] == pos_color:
					queue.append((i, j))
	return image
