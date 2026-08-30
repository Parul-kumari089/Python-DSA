# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        left = 0
        right = mountainArr.length() - 1
        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left
        left = 0
        right = peak
        while left <= right:
            mid = (left + right) // 2
            value = mountainArr.get(mid)
            if value == target:
                return mid
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
        left = peak + 1
        right = mountainArr.length() - 1
        while left <= right:
            mid = (left + right) // 2
            value = mountainArr.get(mid)
            if value == target:
                return mid
            elif value > target:
                left = mid + 1
            else:
                right = mid - 1
        return -1