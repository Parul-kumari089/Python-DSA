class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        ans = []

        for i in range(rowIndex + 1):

            row = [1]

            for j in range(1, i):
                row.append(ans[i-1][j-1] + ans[i-1][j])

            if i > 0:
                row.append(1)

            ans.append(row)

        return ans[rowIndex]