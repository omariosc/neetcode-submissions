class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        candidates = set((r,c) for c in range(COLS) for r in range(ROWS) if grid[r][c])
        if len(candidates) == 0:
            return 0
        
        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                area += dfs(r + dr, c + dc)
            return area

        maxArea = 1
        for r, c, in candidates:
            if grid[r][c] == 1:
                area = dfs(r, c)
                maxArea = max(maxArea, area)
        return maxArea