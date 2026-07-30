class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def cost(minutes, seconds):
            if minutes > 99 or seconds > 99:
                return float('inf')
            digits = f"{minutes:02d}{seconds:02d}"
            # Remove leading zeros but keep at least one digit
            i = 0
            while i < 3 and digits[i] == '0':
                i += 1
            digits = digits[i:]
            finger = str(startAt)
            ans = 0
            for d in digits:
                if finger != d:
                    ans += moveCost
                ans += pushCost
                finger = d
            return ans
        m = targetSeconds // 60
        s = targetSeconds % 60
        answer = cost(m, s)
        if m > 0 and s + 60 <= 99:
            answer = min(answer, cost(m - 1, s + 60))
        return answer
        