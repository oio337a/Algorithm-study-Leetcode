public class SingleNumber_136 {
    public int singleNumber(int[] nums) {
        int len = nums.length;
        int d = 0;
        for (int i = 0; i < len; i++) d = d ^ nums[i];
        return d;
    }

    public static void main(String[] args) {
        int[] nums = {4,2,4,2,1,1,721,721,721,4,4};
        SingleNumber_136 tmp = new SingleNumber_136();
        System.out.println( tmp.singleNumber(nums) );
    }
}
