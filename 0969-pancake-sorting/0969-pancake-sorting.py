from  typing import List
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []       
        for size in range(len(arr), 1, -1):         
            maxIndex = arr.index(max(arr[:size]))
            if maxIndex == size - 1:
                continue
            arr[:maxIndex + 1] = reversed(arr[:maxIndex + 1])
            ans.append(maxIndex + 1)
            arr[:size] = reversed(arr[:size])
            ans.append(size)
        return ans