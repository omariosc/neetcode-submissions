from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                X, Y = int(i/3), int(j/3)
                if (board[i][j] in rows[i] or
                    board[i][j] in cols[j] or
                    board[i][j] in boxes[X][Y]):
                    return False
                boxes[X][Y].add(board[i][j])
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
        
        
        return True