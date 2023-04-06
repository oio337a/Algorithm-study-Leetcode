package LeetCode;
public class BinarySearch_704 {
    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;
        if (end == -1) return -1;
        while (start <= end)
        {
            int mid = start + (end - start) / 2;
            if (nums[mid] > target) end = mid - 1;
            else if (nums[mid] == target) return mid;
            else start = mid + 1;
        }
        return -1;
    }
}
