from typing import List

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         res = 0
#         for i in range(len(height) - 1):
#             for j in range(i + 1, len(height)):
#                 container = min(height[i], height[j]) * (j - i)
#                 res = max(res, container)
#         return res
# 위의 방식으로 풀었더니 시간 초과가 나왔다 
# 당연한 결과 였다 왜냐하면 브루트 포스로 완전탐색이기 때문
# 그래서 이분 탐색을 하기로 했다

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0 , len(height) - 1
        res = 0
        while left <= right:
            container = min(height[left], height[right]) * (right - left)
            res = max(res, container)
            if height[right] > height[left]: # 분기점이 height에 대한 비교
                left += 1
            else :
                right -= 1
        return res

test = Solution()
print(test.maxArea([1,8,6,2,5,4,8,3,7]))
print(test.maxArea([1,2,1]))