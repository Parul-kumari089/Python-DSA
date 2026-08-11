class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        num = 1
        colstart = 0
        rowstart = 0
        colend = n - 1
        rowend = n - 1
        while rowstart <= rowend and colstart <= colend:   
            for i in range(colstart, colend + 1):
                matrix[rowstart][i] = num
                num += 1
            rowstart += 1
            for i in range(rowstart, rowend + 1):
                matrix[i][colend] = num
                num += 1
            colend -= 1
            if rowstart <= rowend:
                for i in range(colend, colstart - 1, -1):
                    matrix[rowend][i] = num
                    num += 1
                rowend -= 1
            if colstart <= colend:
                for i in range(rowend, rowstart - 1, -1):
                    matrix[i][colstart] = num
                    num += 1
                colstart += 1
        return matrix