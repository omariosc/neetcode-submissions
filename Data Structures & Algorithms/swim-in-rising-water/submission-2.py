class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:      
        seen = set()
        pq = [(grid[0][0], (0, 0))]
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        while pq:
            cost, (r, c) = heapq.heappop(pq)
            if (r, c) == (len(grid)-1, len(grid)-1):
                return cost
            if (r,c) not in seen:
                seen.add((r,c))

                for dr, dc in dirs:
                    nr, nc  = dr + r, dc + c
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid) and (nr, nc) not in seen:
                        heapq.heappush(pq, (max(cost, grid[nr][nc]), (nr,nc)))
        return grid[-1][-1]