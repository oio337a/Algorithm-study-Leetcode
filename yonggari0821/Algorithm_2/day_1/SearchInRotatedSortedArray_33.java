public class SearchInRotatedSortedArray_33 {
    static int BS(int[] nums, int target, int initLeft, int initRight)
    {
        int p = -1;
        while (initLeft <= initRight)
        {
            int mid = initLeft + (initRight - initLeft) / 2;
            if (nums[mid] > target) initRight = mid - 1;
            else if (nums[mid] < target) initLeft = mid + 1;
            else
            {
                p = mid;
                break;
            }
        }
        return p;
    }
    public int search(int[] nums, int target) {
        int pos = -1;
        int len = nums.length;
        if (len == 0) return pos;
        else if (len == 1)
        {
            if (nums[0] == target) return 0;
            else return pos;
        }
        int maxIndex = 0;
        for (int i = 1; i < len; i++) {
            if (nums[i] > nums[i-1]) maxIndex = i;
            if (nums[i] == target) return i;
            else break;
        }
        int left = 0;
        int right = nums.length - 1;
        if (nums[left] <= target && target <= nums[maxIndex]) pos = BS(nums, target, left, maxIndex);
//        else if (nums[maxIndex + 1] <= target && target <= nums[right]) pos = BS(nums, target, maxIndex + 1, right); // 이렇게 하면 ArrayOutofBound 에러
        else pos = BS(nums, target, maxIndex + 1, right);
        return pos;
    }

    public int searchByRealBS(int[] nums, int target) {
        int start = 0, end = nums.length - 1;
        int mid = (start + end) / 2;
        while (start <= end) {
            mid = (start + end) / 2;
            if (target == nums[mid]) return mid; // 값 찾음
            if (nums[start] <= nums[mid]) // start ~ mid 무조건 오름차순
            {
                if (nums[start] <= target && target <= nums[mid]) end = mid - 1; // 구간 확정 가능!
                else start = mid + 1; // 구간 확정 불가능
            }
            else // nums[mid] < nums[start] // mid ~ end 무조건 오름차순
            {
                if (nums[mid] <= target && target <= nums[end] ) start = mid + 1; // 구간 확정 가능!
                else end = mid - 1; // 구간 확정 불가능
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] nums1 = {6,7,0,1,2,4,5};
        int target1 = 0;
        int[] nums2 = {2,4,5,6,7,0,1};
        int target2 = 3; // -1
        int[] nums3 = {1};
        int target3 = 0; // -1
        SearchInRotatedSortedArray_33 tmp = new SearchInRotatedSortedArray_33();
        System.out.println(tmp.searchByRealBS(nums1, target1));
    }
}
