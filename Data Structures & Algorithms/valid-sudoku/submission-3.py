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
        grids = {}
        for i in range(y):
            for j in range(x):
                val = board[i][j]
                if val == ".":
                    continue

                grid_x, grid_y = int(i/3), int(j/3)
                key = (grid_x,grid_y)

                if key not in grids:
                    grids[key] = set()
                
                if val in grids[key]:
                    return False

                grids[key].add(val)
        print(grids)
        return True
                
            