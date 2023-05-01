/*
첫 접근은 일반적인 이분탐색 -> 중간지점 기준으로 양쪽 나눠서 검수
근데 같은 로직을 두번 도는게 불필요하다고 생각해서 좀 늦게나오더라도
이분탐색 도중 target을 만나면 그 지점을 start로 세팅, target에서 벗어날 때까지 1씩 더하면서 end의 idx를 찾기
 */
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int start = -1;
        int end;

        if (nums.length == 1 && target == nums[0])
            return (new int[]{0, 0});
        while (left <= right)
        {
            int mid = (left + right) / 2;
            if (nums[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
            if (nums[mid] == target)
            {
                start = mid;
                end = start; // 일단 찾았으니까 end도 시발점으로 설정
                mid++;
                while(mid < nums.length && nums[mid] == target) // mid를 넘기고, target이 아닌 지점에 닿을 때까지 idx 밀기
                {
                    end++;
                    mid++;
                }
            }
        }
        return (new int[]{start, end});
    }
}