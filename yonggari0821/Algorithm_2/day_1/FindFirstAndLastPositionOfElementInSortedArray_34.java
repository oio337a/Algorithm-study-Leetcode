public class FindFirstAndLastPositionOfElementInSortedArray_34 {
    public int[] searchRange(int[] nums, int target) {
        int[] whereIsTheTarget = {-1, -1};
        int left = 0;
        int right = nums.length - 1;
        while (left <= right)
        {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) left = mid + 1;
            else if (nums[mid] == target)
            {
                int tleft = mid;
                int tright = mid;
                while (tleft >= 0 && nums[tleft] == target) tleft--;
                tleft++;
                while (tright < nums.length && nums[tright] == target) tright++;
                tright--;
                whereIsTheTarget[0] = tleft;
                whereIsTheTarget[1] = tright;
                break;
            }
            else right = mid - 1;
        }
        return whereIsTheTarget;
    }

    public int[] searchRangeByDoubleBinarySearch(int[] nums, int target) {
        int[] whereIsTheTarget = {-1, -1};
        int left = 0;
        int right = nums.length - 1;
        while (left <= right)
        {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) left = mid + 1;
            else if (nums[mid] == target)
            {
                // for left edge
                int tleftLeft = 0;
                int tleftRight = mid;
                while (tleftLeft <= tleftRight)
                {
                    int tleftMid = tleftLeft + (tleftRight - tleftLeft) / 2;
                    if (nums[tleftMid] < target) tleftLeft = tleftMid + 1;
                    else // (nums[tleftMid] > target)
                        tleftRight = tleftMid - 1;
                }
                whereIsTheTarget[0] = tleftRight + 1;
                // for right edge
                int trightLeft = mid;
                int trightRight = nums.length - 1;
                while (trightLeft <= trightRight)
                {
                    int trightMid = trightLeft + (trightRight - trightLeft) / 2;
                    if (nums[trightMid] > target) trightRight = trightMid - 1;
                    else // (nums[trightMid] <= target)
                       trightLeft = trightMid + 1;
                }
                whereIsTheTarget[1] = trightLeft - 1;
                break;
            }
            else right = mid - 1;
        }
        return whereIsTheTarget;
    }

    public static void main(String[] args) {
        FindFirstAndLastPositionOfElementInSortedArray_34 tmp = new FindFirstAndLastPositionOfElementInSortedArray_34();
        int[] nums1 = {5,7,7,8,8,10};
        int target1 = 8;
        int[] nums2 = {5,7,7,8,8,10};
        int target2 = 6;
        int[] nums3 = {};
        int target3 = 0;
        // <1>
        System.out.println(tmp.searchRange(nums1, target1)[0] + " " + tmp.searchRange(nums1, target1)[1]);
        System.out.println(tmp.searchRangeByDoubleBinarySearch(nums1, target1)[0] + " " + tmp.searchRangeByDoubleBinarySearch(nums1, target1)[1]);
        // <2>
//        System.out.println(tmp.searchRange(nums2, target2)[0] + " " + tmp.searchRange(nums2, target2)[1]);
//        System.out.println(tmp.searchRange(nums2, target2)[0] + " " + tmp.searchRange(nums2, target2)[1]);
        // <3>
//        System.out.println(tmp.searchRange(nums3, target3)[0] + " " + tmp.searchRange(nums3, target3)[1]);
//        System.out.println(tmp.searchRange(nums3, target3)[0] + " " + tmp.searchRange(nums3, target3)[1]);
    }
}
