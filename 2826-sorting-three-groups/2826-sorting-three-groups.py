class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dp1 = dp2 = dp3 = 0
        for x in nums:
            new1 = dp1 + (x != 1)
            new2 = min(dp1, dp2) + (x != 2)
            new3 = min(dp1, dp2, dp3) + (x != 3)
            dp1, dp2, dp3 = new1, new2, new3
        return min(dp1, dp2, dp3)