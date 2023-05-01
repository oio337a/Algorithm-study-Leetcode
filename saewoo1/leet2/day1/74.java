/* 2차원 배열 안에 1차원 배열 전부다 이분탐색햇서요 */

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int flag = 0;
        int h = matrix.length;
        int i = 0;
        while (i < h)
        {
             if (check_arg(matrix[i], target)) // 하나라도 target과 일치하는 일차원배열이 있다면 true
                return (true);
             i++;
        }
        return (false); // 없다면 false
    }

    private boolean check_arg(int[] nums, int target)
    {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right)
        {
            int mid = (left + right) / 2;
            if (nums[mid] == target)
                return (true);
            if (nums[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return (false);
    }
}