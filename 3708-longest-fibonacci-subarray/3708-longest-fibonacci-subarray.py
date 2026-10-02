class Solution:
    def longestSubarray(self, nums):
        current = 2
        ans = 2
        for i in range(2, len(nums)):
            if nums[i] == nums[i-1] + nums[i-2]:
                current += 1
                ans = max(ans, current)
            else:
                current = 2
        return ans