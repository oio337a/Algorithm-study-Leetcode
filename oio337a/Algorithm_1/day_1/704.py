class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        s = 0
        e = l - 1
        while s <= e:
            mid = (s + e) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        return  -1
