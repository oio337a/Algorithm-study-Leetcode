public class SquaresOfASortedArray_977 {
    public int[] sortedSquares(int[] nums) {
        int len = nums.length;
        int[] output = new int[len];
        int oi = 0;
        int ni = 0;
        while (ni < len && nums[ni] < 0) ni++;
        if (ni == 0) // 모두 양수
        {
            for (int i = 0; i < len; i++)
                output[oi++] = nums[i] * nums[i];
        }
        else if (ni == len) // 모두 음수
        {
            for (int i = len - 1; i >= 0; i--)
                output[oi++] = nums[i] * nums[i];
        }
        else
        {
            int left = ni - 1;
            int right = ni;
            while (left >= 0 && right < len)
            {
                if (-1 * nums[left] >= nums[right])
                {
                    output[oi++] = nums[right] * nums[right];
                    right++;
                }
                else
                {
                    output[oi++] = nums[left] * nums[left];
                    left--;
                }
            }
            if (left < 0)
            {
                while (right < len)
                {
                    output[oi++] = nums[right] * nums[right];
                    right++;
                }
            }
            else if (right == len)
            {
                while (left >= 0)
                {
                    output[oi++] = nums[left] * nums[left];
                    left--;
                }
            }
        }
        return output;
    }
}

class OtherSolution
{
    public int[] sortedSquare(int[] nums)
    {
        int[] output = new int[nums.length];
        int oi = nums.length - 1;
        int left = 0;
        int right = nums.length - 1;
        int tlv = nums[left] * nums[left];
        int trv = nums[right] * nums[right];
        while (left <= right)
        {
            if (tlv >= trv)
            {
                output[oi++] = tlv;
                tlv = nums[++left] * nums[left];
            }
            else
            {
                output[oi++] = trv;
                trv = nums[--right] * nums[right];
            }
        }
        return output;
    }
}
