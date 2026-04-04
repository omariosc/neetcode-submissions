class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        queue = collections.deque()
        queue.append((0,0))
        paths = 0

        while queue:
            row, col = queue.popleft()
            if row == ROWS - 1 and col == COLS - 1:
                paths += 1
            
            directions = [[1,0],[0,1]] # 1D, 1R
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if nr == ROWS or nc == COLS or obstacleGrid[nr][nc] == 1:
                    continue

                queue.append((nr,nc))
        return paths