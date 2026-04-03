class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.sums = []
        for i, row in enumerate(matrix):
            total = 0
            rowSums = []
            for n in row:
                total += n
                rowSums.append(total)
            if i > 0:
                rowSums = [x + y for x, y in zip(rowSums, self.sums[-1])]
            self.sums.append(rowSums)
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        UL = self.sums[row1-1][col1-1] if min(row1,col1) > 0 else 0
        UR = self.sums[row1-1][col2] if row1 > 0 else 0
        LL = self.sums[row2][col1-1] if col1 > 0 else 0
        LR = self.sums[row2][col2]
        return LR - LL - UR + UL
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)