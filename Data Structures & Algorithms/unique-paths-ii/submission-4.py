class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [0] * COLS
        dp[COLS-1] = 1

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c < COLS - 1:
                    dp[c] += dp[c+1]
        
        return dp[0]