class Solution:
    from collections import deque

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()  # 큐 생성
        q.append((sr, sc))  # 처음 좌표 큐에 추가
        target_num = image[sr][sc]  # 현재 위치한 칸 color 기억
        dx = [0, 0, 1, -1]  # 방향 좌표
        dy = [1, -1, 0, 0]
        r, c = len(image), len(image[0])  # row, col 길이 구하기
        visited = [[0] * c for _ in range(r)]  # 방문 여부 체크 리스트 생성
        while q:  # q에 값이 존재 할 때까지 반복
            x, y = q.popleft()  # 값 추출
            image[x][y] = color  # 좌표 색 변환
            visited[x][y] = 1  # 방문 체크
            for i in range(4):  # 4방 탐색
                nx = x + dx[i]
                ny = y + dy[i]
                # 범위안에 존재하고 방문하지 않았을 경우
                if nx >= 0 and nx < r and ny >= 0 and ny < c and not visited[nx][ny]:
                    if target_num == image[nx][ny]:  # 해당 칸이 기존 color와 일치할 경우
                        q.append((nx, ny))  # q 에 삽입
        return (image)
