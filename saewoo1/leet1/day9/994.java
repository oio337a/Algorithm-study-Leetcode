class Solution {
    public int orangesRotting(int[][] grid) {
        int[][] dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int m = grid.length;
        int n = grid[0].length;
        int min = 0;
        Queue<int[]> xy = new LinkedList<>();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2)
                    xy.add(new int[]{i, j, min}); // 썩은애들 좌표 담아
            }
        }
        /* bfs 마스터를 위한 발걸음을 내딛는 중에 룡민님의 도움으로 마무리 지었는대요
            제 코드의 문제점은 min을 for문을 돌면서 2로 바뀌었을 때 min을 더해주는 방식으로 수행했는데
            이러면 depth 기준이 아니라 2로 바꿨을 때 그 횟수만큼 min이 증가하는 오류가 있읍니다
            그래서 unrotten orange으 개수를 갖고 빼면서 돌아야 하나싶었는데
            큐에 min을 넣은 후에 좌표를 변경시킬 때 min을 증가시키면 depth 기준으로 min이 증가가 되니까, 문제가 해결됩니다!!!!!! 데박
         */        
        while (!xy.isEmpty()) {
            int[] now = xy.remove();
            for (int[] cur : dir) {
                int x = now[0] + cur[0];
                int y = now[1] + cur[1];
                min = now[2];
                if (x < 0 || x >= m || y < 0 || y >= n 
                    || grid[x][y] == 0 || grid[x][y] == 2) continue;
                grid[x][y] = 2;
                xy.add(new int[]{x, y, min + 1});
                // if (freshOrange(grid) == false)
                //     break;
            }
        }
        if (freshOrange(grid) == true) // 죽어도 안썩는 케이스
            return -1;
        return min;
    }

    private boolean freshOrange(int[][] grid) { // 하나라도 안썩은 애가 있는지 검사
        int m = grid.length;
        int n = grid[0].length;
        int flag = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1)
                    flag = 1;
            }
        }
        return flag == 1 ? true : false;
    }
}