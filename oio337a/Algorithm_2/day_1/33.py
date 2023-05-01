from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e, max_idx = 0, len(nums) - 1, -1 # 초기값 세팅
        if e == -1: # nums 가 비어있을 때
            return -1
        if nums[s] > nums[e]: # nums 가 로테이션 되어있을 때
            while s <= e: # max_idx 찾기 (이진탐색)
                max_idx = (s + e) // 2
                '''
                기준을 맨 뒤에 있는 값으로 확인
                nums = 3,7,8,0,1,2 이 상태 라면
                만약 mid 가 8 일 경우에는 마지막 의 값 2 보다 크므로 s를 오른쪽 옮길 수 있음
                만약 mid 가 0 일 경우에는 마지막 의 값 2 보다 작으므로 e를 왼쪽으로 옯길 수 있음
                '''
                if nums[max_idx] > nums[-1]:
                    s = max_idx + 1
                elif nums[max_idx] < nums[-1]:
                    e = max_idx - 1
                if nums[max_idx] > nums[max_idx + 1]:
                    break
                elif nums[max_idx] < nums[max_idx - 1]:
                    max_idx -= 1
                    break
            if target <= nums[-1]: # target을 보고 s, e 다시 할당
                s, e = max_idx + 1, len(nums) - 1
            else:
                s, e = 0, max_idx
            while s <= e:
                mid = (s + e) // 2
                if nums[mid] > target:
                    e = mid - 1
                elif nums[mid] < target:
                    s = mid + 1
                else:
                    return mid
        else: # nums 가 로테이션 안된 상태 걍 이진 탐색
            while s <= e:
                mid = (s + e) // 2
                if nums[mid] > target:
                    e = mid - 1
                elif nums[mid] < target:
                    s = mid + 1
                else:
                    return mid
        return -1

nums = [3, 1]
target = 1
test = Solution()
print(test.search(nums, target))
