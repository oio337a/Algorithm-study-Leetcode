class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            check = numbers[start] + numbers[end]
            if target == check:
                break
            elif target > check:
                start += 1
            else:
                end -= 1
        return [start + 1, end + 1]
