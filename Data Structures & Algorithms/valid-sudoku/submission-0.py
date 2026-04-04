class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x = len(board[0])
        y = len(board)

        # Check rows first
        for i in range(y):
            seen = set()
            for j in board[i]:
                if j == ".":
                    continue
                if j in seen:
                    return False
                seen.add(j)
        
        # Check columns now
        for j in range(x):
            seen = set()
            for i in range(y):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
                
        # Check 3x3 grids now
        grids = dict()
        for i in range(x):
            for j in range(y):
                grid_x = int(i/3)
                grid_y = int(y/3)
                if str(grid_x,grid_y) not in grids:
                    grids[str(grid_x,grid_y)] = [board[x,y]]
                elif board[x,y] in grids[str(grid_x,grid_y)]:
                    return False
        return True
                
            