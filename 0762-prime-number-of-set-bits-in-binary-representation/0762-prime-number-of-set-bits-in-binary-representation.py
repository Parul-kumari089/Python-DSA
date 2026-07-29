class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        prime = {2, 3, 5, 7, 11, 13, 17, 19}

        ans = 0

        for num in range(left, right + 1):
            count = bin(num).count("1")

            if count in prime:
                ans += 1

        return ans