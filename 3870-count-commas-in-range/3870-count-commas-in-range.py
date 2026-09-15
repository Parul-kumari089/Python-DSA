class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        place = 1000

        while place <= n:
            count += n - place + 1
            place = place * 1000

        return count