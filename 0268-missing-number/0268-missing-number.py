class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n *(n+1)//2 - sum(nums)
        """seen = set(nums)

        for i in range(len(nums) + 1):
            if i not in seen:
                return i"""
        
           