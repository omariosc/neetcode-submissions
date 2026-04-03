class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        return self.dfs(grid, 0, 0, set())

    def dfs(self, grid: List[List[int]], currentRow, currentCol, visited) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if (currentRow < 0 or currentCol < 0 or
            currentRow == ROWS or currentCol == COLS or
            (currentRow, currentCol) in visited or
            grid[currentRow][currentCol] == 1):
            return 0
        if currentRow == ROWS - 1 and currentCol == COLS - 1:
            return 1

        visited.add((currentRow, currentCol))
        
        count = 0
        count += self.dfs(grid, currentRow+1, currentCol, visited)
        count += self.dfs(grid, currentRow-1, currentCol, visited)
        count += self.dfs(grid, currentRow, currentCol+1, visited)
        count += self.dfs(grid, currentRow, currentCol-1, visited)

        visited.remove((currentRow, currentCol))
        return count