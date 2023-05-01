class Solution {
	public void moveZeroes(int[] nums) {
			int zero = 0;
			for (int i = 0; i < nums.length; i++) { // 0을 어디서부터 채워야할지 찾으면서 0이 아닌 숫자들만 앞으로 다 땡겨옴
					if (nums[i] != 0) {
							nums[zero] = nums[i];
							zero++;
					}
			}
			for (int i = zero; i < nums.length; i++) // 숫자들이 앞으로 다 땡겨졌으면 나머지 공간을 0으로 채움 Arrays.fill 함수랑 동일 의미
					nums[i] = 0;
	}
}