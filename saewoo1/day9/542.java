class Solution {
    /* 첨에 dfs로 재귀 돌면서 했는데 depth가 넘 ㅜ깊어서 터져버림.. bfs 마스터될게요 */
    public int[][] updateMatrix(int[][] mat) {
        final int[][] dir = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
		Queue<int[]> coordinateQueue = new LinkedList<>();
        int m = mat.length;
        int n = mat[0].length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] < 1) // 0들의 좌표를 담아둔 queue
                    coordinateQueue.add(new int[]{i, j});
                else { // 0이 아닌 다른 수라면 
                    mat[i][j] = -1; // 닿을 수 없는 수로 마킹을 해둔다
                }
            }
        }
        while (!coordinateQueue.isEmpty()) {
            int[] now = coordinateQueue.remove();
            for (int[] corrdi : dir) {
                int x = now[0] + corrdi[0];
                int y = now[1] + corrdi[1];
                if (x < 0 || x >= m || y < 0 || y >= n || mat[x][y] > -1) // 마킹한 수 아님? 넘어가
                    continue;
                coordinateQueue.add(new int[]{x, y}); // 0을 기준으로 잡았으니까 그 거리를 더해주고, que에 추가한다
                mat[x][y] = mat[now[0]][now[1]] + 1;
            }
        }
        return mat;
    }
}