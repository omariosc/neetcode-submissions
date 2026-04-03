class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        if len(word) == 1:
            return any(board[i][j] == word[0] for i in range(ROWS) for j in range(COLS))

        def dfs(r, c, i, visited):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visited or board[r][c] != word[i]:
                return False
            
            visited.add((r,c))
            res = (
                dfs(r+1, c, i+1, visited) or
                dfs(r, c+1, i+1, visited) or
                dfs(r-1, c, i+1, visited) or
                dfs(r, c-1, i+1, visited)
            )
            visited.remove((r,c))
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, set()):
                        return True
        return False