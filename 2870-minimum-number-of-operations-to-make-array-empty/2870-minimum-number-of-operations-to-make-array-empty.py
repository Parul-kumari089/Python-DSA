from collections import Counter
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        operations = 0
        for count in freq.values():
            if count == 1:
                return -1
            if count % 3 == 0:
                operations += count // 3
            elif count % 3 == 1:
                operations += (count - 4) // 3 + 2
            else: 
                operations += count // 3 + 1
        return operations