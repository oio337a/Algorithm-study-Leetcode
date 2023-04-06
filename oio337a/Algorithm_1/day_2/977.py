class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        li = []
        for num in nums:
            li.append(num**2)
        return sorted(li)