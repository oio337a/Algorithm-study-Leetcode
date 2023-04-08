import java.util.Arrays;

public class TwoSome2_167 {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;
        int[] leftAndRight = new int[2];
        while (left < right)
        {
            int sum = numbers[left] + numbers[right];
            if (sum > target) right--;
            else if (sum == target) {
               leftAndRight[0] = left + 1;
               leftAndRight[1] = right + 1;
               break;
            }
            else left++;
        }
        return leftAndRight;
    }

    public int[] twoSumByBinarySearch(int[] numbers, int target)
    {
        int left = 0;
        int right = numbers.length - 1;
        while (left < right)
        {
            int mid = left + (right - left) / 2;
            int sum = numbers[left] + numbers[right];
            if (sum > target)
            {
                if (numbers[mid] >= target - numbers[left]) right = mid;
                else right--;
            }
            else if (sum == target) {
                int[] leftAndRight = new int[2];
                leftAndRight[0] = left + 1;
                leftAndRight[1] = right + 1;
                return leftAndRight;
            }
            else
            {
                if (numbers[mid] <= target - numbers[right]) left = mid;
                else left++;
            }
        }
        return null;
    }

    public static void main(String[] args) {
        TwoSome2_167 tmp = new TwoSome2_167();
        int[] nums = {2, 3, 3, 3, 3, 3, 5, 7, 11, 15};
        int target = 9;
        System.out.println(Arrays.toString(tmp.twoSumByBinarySearch(nums, target)));
    }
}

/*
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
 */