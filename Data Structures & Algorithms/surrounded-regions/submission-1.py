class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(x, y):
            if x < 0 or x == ROWS or y < 0 or y == COLS or board[x][y] != "O":
                return

            board[x][y] = "#"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
