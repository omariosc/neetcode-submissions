class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        board = [["."] * n for _ in range(n)]

        pos_diag, neg_diag, columns = set(), set(), set()
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                self.res.append(copy)
                return

            for c in range(n):
                if c in columns or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                columns.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                columns.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return self.res