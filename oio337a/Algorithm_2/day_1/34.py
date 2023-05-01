from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s, e = 0, len(nums) - 1
        s_range, e_range = -1, -1 # return할 변수 선언 및 초기화
        if (e == -1): # 배열이 들어오지 않았을 경우
            return [s_range, e_range]
        while (s <= e): # 이진탐색 시작
            mid = (s + e) // 2 # 중간값 설정
            if nums[mid] > target:
                e = mid - 1
            elif nums[mid] < target:
                s = mid + 1
            else: # target 이 맞는 경우
                s_range = mid
                while nums[s_range] == target: # 시작 지점 찾기
                    s_range -= 1
                    if s_range < 0: # 인덱스 벗어나는 경우
                        break
                while nums[mid] == target: # 끝 지점 찾기
                    mid += 1
                    if mid > len(nums) - 1: # 인덱스 벗어나는 경우
                        break
                e_range = mid
                return [s_range + 1, e_range - 1] # 해당 값 반환
        return [s_range, e_range] # 찾는 값이 없는 경우 -1, -1 반환


nums = []
target = 0
test = Solution()
print(test.searchRange(nums, target))