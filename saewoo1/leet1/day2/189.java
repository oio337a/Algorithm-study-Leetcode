class Solution {
    public void rotate(int[] nums, int k) {
        int[] arr = new int[nums.length];
        for (int i = 0; i < arr2.length; i++)
            arr[(i + k) % nums.length] = nums[i];
        for (int i = 0; i < nums.length; i++)
            nums[i] = arr[i];
		// char 배열로 변환 후에 reverse로 풀고싶었는데 지원 안해준대여
		// idx 변환은 똑같음
    }
}