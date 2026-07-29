class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 
        x = n 
        while x:
            x &= (x-1)
            count += 1
        return count 