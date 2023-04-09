class Solution {
	public int[] twoSum(int[] numbers, int target) {
	/* suhwpark 아이디어 버억했습니다
	 * 더한 값이 target보다 크면 right를 줄이고, 작으면 left를 늘려서 값을 조정하며 합해서 target이 되는 지점을 찾습니다.
	 * left, right는 idx로 사용했으니 res에 넣을 땐 1씩 더한 후 반환합니다
	 */
	 int    left = 0;
	 int    right = numbers.length - 1;
	 int[] res = new int[2];
	 for (int i = 0; i < numbers.length; i++)
	 {
		 if (numbers[left] + numbers[right] == target)
		 {
				 res[0] = left + 1;
				 res[1] = right + 1;
		 }
		 else if (numbers[left] + numbers[right] > target)
				right--;
		 else if (numbers[left] + numbers[right] < target)
				left++;
	 }
	 return res;
	}
}