class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        q = []
        heapq.heapify(q)
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((0,r,c))

        while q:
            distance, r, c = heapq.heappop(q)
            if distance != 0 and distance < grid[r][c]:
                grid[r][c] = distance
            for dr, dc in [(1,0), (-1,0), (0,-1), (0,1)]:
                if 0 <= r + dr < ROWS and 0 <= c + dc < COLS:
                    if grid[r+dr][c+dc] == INF:
                        heapq.heappush(q, (distance+1, r+dr, c+dc))