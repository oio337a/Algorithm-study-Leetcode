import java.util.Arrays;

public class MoveZeroes_283 {
    public void moveZeroes(int[] nums) {
        int len = nums.length;
        int i = 0;
        while(i < len)
        {
            if (nums[i] == 0)
            {
                for (int j = i + 1; j < len; j++)
                {
                    if (nums[j] != 0)
                    {
                        nums[i] = nums[j];
                        nums[j] = 0;
                        break;
                    }
                    if (j == len - 1) return;
                }
            }
            i++;
        }
    }

    public void moveZeroesByPuttingNotZeroes(int[] nums)
    {
        int len = nums.length;
        int zi = 0;
        for (int i = 0; i < len; i++)
        {
            if (nums[i] != 0)
            {
                if (i != zi)
                {
                    nums[zi] = nums[i];
                    nums[i] = 0;
                }
                zi++;
            }
        }
    }

    public static void main(String[] args) {
        int[] nums = {1, -99, 0, 8, 0, 12};
        MoveZeroes_283 tmp = new MoveZeroes_283();
        tmp.moveZeroesByPuttingNotZeroes(nums);
        System.out.println(Arrays.toString(nums));
    }
}

/*
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
1 0 0 3 12
1 3 0 0 12
1 3 12 0 0
//
1 0 0 3 12
1 3 0 0 12


Input: nums = [1, -99, 0, 8, 0, 12]
Output: [1, -99, 12, 0, 0, 0]
1 -99 8 0 0 12
1 -99 8 12 0 0
 */