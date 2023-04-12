/*
    1. m x n 크기의 사각형
    2. sr(start row?), sc(start column), color가 주어진다.
    3. sr, sc부터 시작해서 사각형을 채워 나가기 시작한다.
    4. color로 채워나가는 조건은 sr, sc 위치부터 4방향 중 시작점과 같은 수를 지니고 있다면, sr, sc의 값을 new color로(칠한다) DFS?
*/

class Solution {
	public int[][] floodFill(int[][] image, int sr, int sc, int color) {
		if (image[sr][sc] == color) // 이미 시작점의 색상과 newcolor가 동일하다면 더 칠할 필요 없으니 종료
			return image;
		fill_square(image, sr, sc, image[sr][sc], color); // 시작 컬러와 칠할 컬러가 다르니 start 기준 4방향을 검수하는 dfs를 돈다
		return image;
	}

	private void fill_square(int[][] image, int sr, int sc, int oldColor, int newColor) {
		/*
		 * 재귀가 종료될 조건은
		 * sr, sc를 빼거나 더하면서 탐색할 때 0보다 작거나 주어진 m, n의 범위를 넘어갈 때
		 * 기준의 4방향에서 애초에 같지 않은 수일 때(재귀를 아예 돌 필요가 없는 케이스)
		 */
		if (sr < 0 || sc < 0 || sr >= image.length || sc >= image[0].length
				|| image[sr][sc] != oldColor)
			return;
		image[sr][sc] = newColor; // start가 newcolor와 같지 않은 케이스들만 여기 들와 계속 칠할꺼니까 시작점을 newcolor로 변경해놓고 4방향을 탐색한다
		fill_square(image, sr - 1, sc, oldColor, newColor);
		fill_square(image, sr + 1, sc, oldColor, newColor);
		fill_square(image, sr, sc - 1, oldColor, newColor);
		fill_square(image, sr, sc + 1, oldColor, newColor);
	}
	/*
	 * 1 1 1
	 * 1 2 0
	 * 1 0 1
	 * fill(image, 0, 1, 1, 2); image[sr - 1][sc] = 2
	 * 1 2 1
	 * 1 2 0
	 * 1 0 1
	 * fill(image -1) 터짐 위쪽 탐색 종료
	 * fill(image 2, 1, 1, 2) image[2][1] = 0, != 1 현재 컬러와 같지 않다 아래 탐색 종료
	 * fill(1, 0, 1, 2) image[1][0] = 1 -> 2
	 * 1 2 1
	 * 2 2 0
	 * 1 0 1
	 * 아 하나씩 다보네
	 * 
	 *
	 * 
	 * 
	 */
}

// 같은 로직인데 얘가 왜 더 빨리돌까? 다른 사람꺼 정답입니두

class Solution {

	public int[][] floodFill(int[][] image, int sr, int sc, int color) {
		// edge case
		if (image.length == 0)
			return image;

		int init_c = image[sr][sc]; // oldColor 세팅
		fill(image, sr, sc, color, init_c);
		return image;
	}

	private void fill(int[][] image, int i, int j, int new_color, int init_c) {

		if (i < 0 || j < 0 || i >= image.length || j >= image[0].length || image[i][j] == new_color)
			return;

		if (image[i][j] == init_c) { // 검수하는 위치의 컬러가 oldColor와 일치하는 경우만 검수
			image[i][j] = new_color; // 현재 컬러를 newColor로 세팅하고 검수를 진행한다
			fill(image, i - 1, j, new_color, init_c);
			fill(image, i, j - 1, new_color, init_c);
			fill(image, i, j + 1, new_color, init_c);
			fill(image, i + 1, j, new_color, init_c);
		}

	}
	/*
	 * 1 1 1
	 * 1 1 0
	 * 1 0 1
	 * 
	 * init_c = 1
	 * fill(image, 1, 1, 2, 1) 함수 시작
	 * newcolor = image[1][1] = 2로 세팅
	 * 1 1 1
	 * 1 2 0
	 * 1 0 1
	 * fill(image, 0, 1, 2, 1); 수행 image[0][1] = 2;
	 * 1 2 1
	 * 1 2 0
	 * 1 0 1
	 * fill(image -1, 1, 2, 1) -> 터지니까 return; 위쪽 탐색 종료
	 * fill(image, 1, 0, 2, 1); 수행 image[1][0] = 2;
	 * 1 2 1
	 * 2 2 0
	 * 1 0 1
	 * fill(image 1, -1) 터져서 return; 왼쪽 탐색 종료
	 * 아 천재네 덜도네 위에서 미리 검수하고 아래에서는 진짜 바꿔주기만 해주네
	 */

}