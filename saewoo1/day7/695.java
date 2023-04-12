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