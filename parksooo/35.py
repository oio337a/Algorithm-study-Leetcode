class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1
        if nums[0] > target:
            return 0
        if nums[e] < target:
            return e + 1
        while s <= e:
            mid = (s + e) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[mid - 1] < target and nums[mid] > target:
                    return mid
                e = mid - 1
            else:
                if nums[mid] < target and nums[mid + 1] > target:
                    return mid + 1
                s = mid + 1