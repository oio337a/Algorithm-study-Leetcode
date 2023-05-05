from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0 # 반환값 
        s, e = 0, len(height) - 1 # 초기값 설정 시작, 끝
        while s <= e:
            result = max(result, (e - s) * min(height[s], height[e])) # max 설정

            if height[s] >= height[e]: # 높이가 낮은쪽 확인
                e -= 1
            else:
                s += 1
        return result # max값 반환


height = [1,8,6,2,5,4,8,3,7]
test = Solution()
print(test.maxArea(height))