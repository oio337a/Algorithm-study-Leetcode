import java.util.LinkedList;
import java.util.Queue;

// 0 representing an empty cell
// 1 representing a fresh orange
// 2 representing a rotten orange
class orange
{
    int row;
    int col;

    public orange(int r, int c)
    {
        this.row = r;
        this.col = c;
    }
}

public class RottingOranges_994 {
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    public int orangesRotting(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        Queue<orange> q = new LinkedList<>();
        for (int r = 0; r < row; r++)
        {
            for (int c = 0; c < col; c++)
            {
                if (grid[r][c] == 2)
                {
                    grid[r][c] = 0;
                    q.offer(new orange(r, c));
                }
                else if (grid[r][c] == 1)
                    grid[r][c] = -1;
                else
                    grid[r][c] = -2;
            }
        }
        while (!q.isEmpty())
        {
            orange tmp = q.poll();
            int tr = tmp.row;
            int tc = tmp.col;
            for (int i = 0; i < 4; i++)
            {
                int nr = tr + dr[i];
                int nc = tc + dc[i];
                if (nr < 0 || nc < 0 || nr >= row || nc >= col) continue;
                if (grid[nr][nc] == -1)
                {
                    grid[nr][nc] = grid[tr][tc] + 1;
                    q.offer(new orange(nr, nc));
                }
            }
        }
        int min = 0;
        for (int r = 0; r < row; r++)
        {
            for (int c = 0; c < col; c++) {
                if (grid[r][c] == -1) return -1;
                min = min > grid[r][c] ? min : grid[r][c];
            }
        }
        return min;
    }

    public static void main(String[] args) {
        RottingOranges_994 tmp = new RottingOranges_994();
        int[][] grid = {{2,1,1},{1,1,0},{0,1,1}};
        System.out.println(tmp.orangesRotting(grid));
    }
}
