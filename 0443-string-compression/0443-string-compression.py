class Solution:
    def compress(self, chars: List[str]) -> int:
        n= len(chars)
        i = 0
        index = 0 
        while i<n:
            ch = chars[i]
            count = 0 
            while i < n and chars[i] == ch:
                count += 1
                i += 1
            chars[index] = ch 
            index += 1
            if count > 1:
                for digit in str(count): 
                    chars[index] = digit 
                    index += 1
        return index              
        