class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last = len(nums) - 1
        for i in range(k):
            poped_num = nums.pop(last)
            nums.insert(0, poped_num)