class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:      
        ROWS, COLS = len(grid), len(grid[0])
        if ROWS == 1 and COLS == 1:
            return grid[0][0]
        
        previous = [grid[0][0]]
        for i, top in enumerate(grid[0][1:]):
            previous.append(max(top, previous[i-1]))

        for row in grid[1:]:
            for i, curr in enumerate(row):
                if i == 0:
                    previous[0] = max(curr, previous[0])
                    continue
                previous[i] = max(curr, min(previous[i], previous[i-1]))

        return previous[-1]