class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        visited = set()
        queue = collections.deque()

        visited.add((0,0))
        queue.append((0,0))

        length = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row == ROWS - 1 and col == COLS - 1:
                    return length
                
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                for directionRow, directionCol in directions:
                    if (row + directionRow < 0 or col + directionCol < 0 or 
                        row + directionRow == ROWS or col + directionCol == COLS or
                        (row + directionRow, col + directionCol) in visited or 
                        grid[row + directionRow][col + directionCol] == 1):
                        continue
                    queue.append((row + directionRow, col + directionCol))
                    visited.add((row + directionRow, col + directionCol))
            length += 1
        return -1
