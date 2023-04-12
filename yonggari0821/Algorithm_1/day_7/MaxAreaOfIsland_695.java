import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class MaxAreaOfIsland_695 {
    // 상하좌우 이동용 배열 2개
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    // 최대 값
    static int Max = 50;
    public int maxAreaOfIsland(int[][] grid) {
        int maxLand = 0;
        int rowLen = grid.length;
        int columnLen = grid[0].length;
        // 둘 중에 아무거나로 가능!
        // 스택 => DFS / 큐 => BFS
        // 둘 다 제출해본 결과 시간복잡도와 메모리 측면 모두에서 bfs가 우월!!
//        Queue<Integer> q = new LinkedList<>();
        Stack<Integer> s = new Stack<>();
        for (int r = 0; r < rowLen; r++)
        {
            for (int c = 0; c < columnLen; c++)
            {
                if (grid[r][c] == 1)
                {
                    int cnt = 0;
                    grid[r][c] = 0; // 시작 지점도 바다 처리
//                    q.offer(r * Max + c);
                    s.push(r * Max + c);
//                    while (!q.isEmpty())
                    while (!s.isEmpty())
                    {
//                        int tmp = q.poll();
                        int tmp = s.pop();
                        int nr = tmp / Max;
                        int nc = tmp % Max;
                        cnt++;
//                        System.out.println(nr + " / " + nc + " = " + cnt);
                        for (int i = 0; i < 4; i++)
                        {
                            int tr = nr + dr[i];
                            int tc = nc + dc[i];
                            if (tr < 0 || tc < 0 || tr >= rowLen || tc >= columnLen) continue;
                            if (grid[tr][tc] != 1) continue;
                            grid[tr][tc] = 0; // 여기서 큐나 스택에 넣기 전에 처리 안하고 넣은 다음 빼서 처리하면 중복이 될 우려가 있음!!
//                            q.offer(tr * Max + tc);
                            s.push(tr * Max + tc);
                        }
                    }
                    maxLand = maxLand > cnt ? maxLand : cnt;
                }
            }
        }
        return maxLand;
    }

    public static void main(String[] args) {
        MaxAreaOfIsland_695 tmp = new MaxAreaOfIsland_695();
//        int[][] grid = {{0,0,1,0,0,0,0,1,0,0,0,0,0},{0,0,0,0,0,0,0,1,1,1,0,0,0},{0,1,1,0,1,0,0,0,0,0,0,0,0},{0,1,0,0,1,1,0,0,1,0,1,0,0},{0,1,0,0,1,1,0,0,1,1,1,0,0},{0,0,0,0,0,0,0,0,0,0,1,0,0},{0,0,0,0,0,0,0,1,1,1,0,0,0},{0,0,0,0,0,0,0,1,1,0,0,0,0}};
        int[][] grid = {{1,1,0,0,0}, {1,1,0,0,0}, {0,0,0,1,1}, {0,0,0,1,1}};
        System.out.println(tmp.maxAreaOfIsland(grid));
        System.out.println(Arrays.deepToString(grid)); // 모두 0으로 나와야 함
    }
}
