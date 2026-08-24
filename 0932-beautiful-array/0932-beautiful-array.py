class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n == 1:
            return [1]
        odd = self.beautifulArray((n + 1) // 2)
        even = self.beautifulArray(n // 2)
        result = []
        for x in odd:
            result.append(2 * x - 1)
        for x in even:
            result.append(2 * x)
        return result