class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(grid, r, c):
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == 1:
                return 0
            if r == ROWS-1 and c == COLS-1:
                return 1

            count, grid[r][c] = 0, 1
            count += dfs(grid, r+1, c)
            count += dfs(grid, r-1, c)
            count += dfs(grid, r, c+1)
            count += dfs(grid, r, c-1)

            grid[r][c] = 0
            return count
            
        return dfs(grid, 0, 0)