def rotate(nums: List[int], k: int) -> None:
	for i in range(k):
		p = nums.pop(-1)
		nums.insert(0, p)