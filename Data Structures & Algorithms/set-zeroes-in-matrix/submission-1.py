class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
    
        def makeRowZero(x: int):
            for c in range(n):
                if matrix[x][c] != 0:
                    matrix[x][c] = "X"
        
        def makeColZero(y: int):
            for r in range(m):
                if matrix[r][y] != 0:
                    matrix[r][y] = "X"

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    makeRowZero(r)
                    makeColZero(c)
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "X":
                    matrix[r][c] = 0
