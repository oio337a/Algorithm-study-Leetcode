import java.util.Arrays;

public class RotateArray_189 {
    public void rotate(int[] nums, int k) {
        int len = nums.length;
        int[] output = new int[len];
        for (int i = 0; i < len; i++)
            output[(i + k) % len] = nums[i];
        for (int i = 0; i < len; i++) {
            nums[i] = output[i];
        }
    }

    public void rotateByShuffle(int[] nums, int k)
    {
        int len = nums.length;
        for (int i = 0; i < k; i++)
        {
            int tmp = nums[i];
            nums[i] = nums[len -1 -i];
            nums[len -1 -i] = tmp;
        }
        Arrays.sort(nums, 0, k);
        Arrays.sort(nums, k, len);
    }
    // 참고한 코드

    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5,6,7};
        int k = 3;
        RotateArray_189 rotateArray189 = new RotateArray_189();
        rotateArray189.rotateByShuffle(arr, k);
        System.out.println(Arrays.toString(arr));
    }
}

/*
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

123456789 3
987456123
789123456
 */