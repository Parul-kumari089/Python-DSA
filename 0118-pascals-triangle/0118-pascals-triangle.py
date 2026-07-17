class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            row = [1]
            for j in range(1, i):
                row.append(ans[i-1][j-1] + ans[i-1][j])
            if i > 0:
                row.append(1)

            ans.append(row)

        return ans
        