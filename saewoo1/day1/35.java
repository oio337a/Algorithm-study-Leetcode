class Solution {
    public int searchInsert(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++)
        {
            if (target <= nums[i])
                return (i);
            if (i + 1 < nums.length)
                if (target > nums[i] && target <= nums[i + 1])
                    return (i + 1);
        }
        return (nums.length);
    }
}