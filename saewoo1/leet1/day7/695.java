class Solution { //또 dfs... bfs로도 풀어볼게여..
    public int maxAreaOfIsland(int[][] grid) {
        int area = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] > 0) // 섬이라면 dfs 수행하면서 가장 큰 면적을 찾음
                    area = Math.max(area, getArea(grid, i, j));
            }
        }
        return area;
    }

    private int getArea(int[][] grid, int i, int j) {
        int area = 0;
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] < 1 ) // 범위가 초과되지 않고, 섬이 아니면 area로 추가되지 않음
            return 0;

        grid[i][j] = 0; // 방문 했으니 0으로 변경
        return (1 + getArea(grid, i + 1, j) + getArea(grid, i - 1, j) + getArea(grid, i, j + 1) + getArea(grid, i, j - 1)); // 상하좌우 탐색
    }
}

//----bfs

class Solution {
    private int[][]dir = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

    public int maxAreaOfIsland(int[][] grid) {
        int area = 0;
        int r = grid.length;
        int c = grid[0].length;
        int[][] visited = new int[r][c];

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (visited[i][j] == 0 && grid[i][j] > 0) // 방문한 적이 없고, 현 위치가 섬이라면 최대 크기를 찾아 떠난다
                    area = Math.max(area, getArea(grid, visited, i, j, r, c));
            }
        }
        return area;
    }

    private int getArea(int[][] grid, int[][] visited, int i, int j, int r, int c) {
        int area = 0;
        visited[i][j] = 1; // 방문을 했다고 체크
        Queue<int[]> res = new LinkedList<>(); // que 생성, int 배열 위치 넣어준다
        res.add(new int[]{i, j}); // 현 위치를 넣어준다
        while (!res.isEmpty()) {
			int[] pos = res.remove(); // pos는 가장 앞의 위치를 받아왔음
			area++;
			for (int[] arr : dir) { //4 방향을 순회합니다
				int x = pos[0] + arr[0];
				int y = pos[1] + arr[1];
				if (x >= 0 && x < r && y >= 0 && y < c && grid[x][y] > 0 && visited[x][y] < 1) { // board 내부에 있는 섬이라면
					res.add(new int[]{x, y}); // 위치를 담아주고, 방문했다고 표기해줌
					visited[x][y] = 1;
				}
			}
        }
        return area;
    }
}
