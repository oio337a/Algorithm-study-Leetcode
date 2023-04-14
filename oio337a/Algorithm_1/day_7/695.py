class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # ---- BFS 함수 ---- #
        def BFS(i, j, r, c, grid, visited):
            q = deque()  # q 생성
            q.append([i, j])  # 들어온 초기값 삽입
            dx = [-1, 0, 1, 0]  # 방향 좌표
            dy = [0, 1, 0, -1]
            visited[i][j] = 1  # 현재위치 방문 체크
            island_size = 1  # 시작 땅 크기
            while q:
                x, y = q.popleft()  # 좌표 꺼내기
                for i in range(4):  # 4방 탐색
                    nx, ny = x + dx[i], y + dy[i]  # 다음 좌표 설정
                    # 범위안, 땅, 방문 x 시
                    if 0 <= nx and nx < r and 0 <= ny and ny < c and grid[nx][ny] == 1 and visited[nx][ny] == 0:
                        visited[nx][ny] = 1  # 방문 체크
                        q.append([nx, ny])  # 새로운 좌표 q에 삽입
                        island_size += 1  # 땅크기 + 1
            return island_size
        # ---- 코드 여기서 부터 실행 ---- #
        r, c = len(grid), len(grid[0])  # row, col 길이 저장
        island_size = 0  # 반환값 초기값 설정
        visited = [[0] * c for _ in range(r)]  # 방문 체크 여부 2차원 배열 생성
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:  # grid 를 돌면서 새로운 섬을 만나면 bfs 시작
                    # bfs의 반환값이 그 섬의 땅 크기 max 값으로 갱신
                    island_size = max(island_size, BFS(
                        i, j, r, c, grid, visited))
        return island_size
