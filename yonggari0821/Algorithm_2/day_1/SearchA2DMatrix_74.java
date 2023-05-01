public class SearchA2DMatrix_74 {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rstart = 0;
        int rend = matrix.length - 1;
        int columnEnd = matrix[0].length - 1;
        while (rstart <= rend)
        {
            int rmid = rstart + (rend - rstart) / 2;
            int tmpleft = matrix[rmid][0];
            int tmpright = matrix[rmid][columnEnd];
            if (tmpleft <= target && target <= tmpright)
            {
                int columnStart = 0;
                while (columnStart <= columnEnd)
                {
                    int columnMid = columnStart + (columnEnd - columnStart) / 2;
                    if (matrix[rmid][columnMid] == target) return true;
                    else if (matrix[rmid][columnMid] > target) columnEnd = columnMid - 1;
                    else columnStart = columnMid + 1;
                }
            }
            else if (target < tmpleft) rend = rmid - 1;
            else if (target > tmpright) rstart = rmid + 1;
        }
        return false;
    }

    public static void main(String[] args) {
        SearchA2DMatrix_74 tmp = new SearchA2DMatrix_74();
        int[][] matrix = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
        int target = 3;
        System.out.println(tmp.searchMatrix(matrix, target));
    }
}
