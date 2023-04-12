import java.util.Arrays;
import java.util.Stack;

public class FloodFill_733 {
    // 상하좌우 이동용 배열 2개
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    // 최대 50 * 50 이므로 x * Max + y의 값으로 좌표 구함
    static int Max = 50;

    public int[][] floodFill(int[][] image, int sr, int sc, int color)
    {
        int original = image[sr][sc]; // 판단용, 처음위치의 color
        if (original == color) return image;
        int rowLen = image.length; // 매개변수로 들어오는 배열 전체 행 길이
        int columnLen = image[0].length; // 매개변수로 들어오는 배열 전체 열 길이
        boolean[][] visited = new boolean[rowLen][columnLen]; // 방문 확인용 배열
        Stack<Integer> stack = new Stack<>(); // Stack 구조를 이용해서 풀 예정! (LIFO 구조 활용)
        stack.push(sr * Max + sc); // 처음위치 값 넣어주고 시작
        while (!stack.isEmpty())
        {
            int tmp = stack.pop();
            int r = tmp / Max; // 행 값
            int c = tmp % Max; // 열 값
            visited[r][c] = true; // 방문처리
            image[r][c] = color; // 색칠처리
            for (int i = 0; i < 4; i++)
            {
                int tr = r + dr[i];
                int tc = c + dc[i];
                if (tr < 0 || tc < 0 || tr >= rowLen || tc >= columnLen) continue; // 범위 벗어나면 pass
                if (visited[tr][tc] == true) continue; // 방문한 적이 있으면 pass
                if (image[tr][tc] == original) stack.push(tr * 50 + tc);
            }
        }
        return image;
    }

    // 왜 방문처리도 없고, 스택을 활용하지도 않는 단순 재귀로 구현한 코드가 더 빠른지 잘 모르겠습니다 ㅠ

    public static void main(String[] args) {
        FloodFill_733 tmp = new FloodFill_733();
        int[][] image = {{1,1,1},{1,1,0},{1,0,1}};
        System.out.println(Arrays.deepToString(tmp.floodFill(image, 1, 1, 2)));
    }
}
