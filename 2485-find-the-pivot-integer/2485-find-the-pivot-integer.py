class Solution:
    def pivotInteger(self, n: int) -> int:

        total = n * (n + 1) // 2
        leftSum = 0
        for x in range(1, n + 1):
            leftSum += x
            rightSum = total - leftSum + x

            if leftSum == rightSum:
                return x

        return -1
        