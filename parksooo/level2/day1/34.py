from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int] :
        def search_pos(nums: List[int], target: int)-> int:
            s = 0
            e = len(nums) - 1
            while s <= e:
                mid = (s + e) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    s = mid + 1
                else :
                    e = mid - 1
            return -1
    
        pos = search_pos(nums, target) # 이진 탐색으로 타겟 위치 찾기
        if pos == -1: # 없으면 리턴
            return [-1, -1]
        s = e = pos # 스타트 엔드 값을 pos로 정하고 while문을 두번 돌려서 타겟의 시작과 끝을 찾는다
        while e < len(nums) - 1 and nums[e] == target:
            if nums[e + 1] == target:
                e += 1
            else :
                break
        i = 0
        while i < s:
            if nums[i] == target:
                s = i
                break
            i += 1
        return [s, e]

test = Solution()
print(test.searchRange([5,7,7,8,8,10], 8))
print(test.searchRange([1], 1))
print(test.searchRange([1, 1], 1))