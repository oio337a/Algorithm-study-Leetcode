# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        s = 0
        e = n
        while True:
            mid = (s + e) // 2
            if not isBadVersion(mid - 1) and isBadVersion(mid):
                return mid
            elif isBadVersion(mid):
                e = mid - 1
            else :
                s = mid + 1