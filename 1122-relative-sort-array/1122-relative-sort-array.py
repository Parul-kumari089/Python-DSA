from collections import Counter

class Solution:
    def relativeSortArray(self, arr1, arr2):
        freq = Counter(arr1)
        ans = []
        for num in arr2:
            ans.extend([num] * freq[num])
            del freq[num]
        for num in sorted(freq):
            ans.extend([num] * freq[num])
        return ans