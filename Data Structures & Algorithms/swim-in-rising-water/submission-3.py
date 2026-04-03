class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        pq = [(grid[0][0], (0, 0))]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while pq:
            cost, (r, c) = heapq.heappop(pq)
            
            if r == ROWS - 1 and c == COLS - 1:
                return cost
            
            if (r, c) not in seen:
                seen.add((r,c))
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in seen:
                        heapq.heappush(pq, (max(cost, grid[nr][nc]), (nr, nc)))