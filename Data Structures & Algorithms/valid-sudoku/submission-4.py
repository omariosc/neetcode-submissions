from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        for i in range(ROWS):
            seen = set()
            for j in range(COLS):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        for i in range(COLS):
            seen = set()
            for j in range(ROWS):
                if board[j][i] == ".":
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])

        grid = defaultdict(set)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == ".":
                    continue
                X, Y = int(i/3), int(j/3)
                if board[i][j] in grid[(X,Y)]:
                    return False
                grid[(X,Y)].add(board[i][j])
        
        
        return True