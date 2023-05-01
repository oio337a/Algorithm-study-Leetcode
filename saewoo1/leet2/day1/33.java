class Solution {
    public int search(int[] nums, int target) {
        /*
			일단 로테이션이라는거 자체에서 연속된 수는 어느정도 정렬이 되어있다는 보장을 받음
			범위를 mid를 기준으로 나누고, target이 left사이 에 있는지, right 사이에 있는지 확인
			찾았다면, right, left 값을 조절해 범위를 줄이며 다시 이분탐색
		 */

        int left = 0;
        int right = nums.length - 1;
        while (left <= right)
        {
            int mid = (right + left) / 2;
            if (nums[mid] == target)
                return (mid);
            if (nums[left] <= nums[mid]) // 이 범위는 정렬이 됐구나 보장받음
            {
                if (nums[left] <= target && nums[mid] > target) // left와 mid 범위 사이에 target이 존재한다면
                    right = mid - 1; // left는 고정시키고, right의 범위를 줄인다
                else
                    left = mid + 1; // target이 그 사이값이 아니라면, left를 mid 다음으로 넘기고 재탐색
            }
            else // 반대로 nums[right] > nums[mid]로 뒷부분이 정렬이 됐다고 판별이 나면
            {
                if (nums[right] >= target && nums[mid] < target) // 이 사이에 target이 존재하는가?
                    left = mid + 1; // 존재한다면 right를 고정시키고, left 범위를 줄인다
                else
                    right = mid - 1; // 존재하지 않는다면, right의 범위를 mid 전으로 옮겨 범위를 줄인다
            } // mid를 기준으로 left, right를 옮겼으니 정렬된 부분을 찾을 수밖에 없음을 보장받읍니다
        }
        return (-1);
    }
}