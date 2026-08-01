class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(ans - target):
                    ans = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
        return ans