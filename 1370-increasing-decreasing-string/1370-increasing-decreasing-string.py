class Solution:
    def sortString(self, s: str) -> str:
        freq = [0] * 26

        
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        ans = []

        while len(ans) < len(s):

            
            for i in range(26):
                if freq[i] > 0:
                    ans.append(chr(i + ord('a')))
                    freq[i] -= 1

            
            for i in range(25, -1, -1):
                if freq[i] > 0:
                    ans.append(chr(i + ord('a')))
                    freq[i] -= 1

        return ''.join(ans)