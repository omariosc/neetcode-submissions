class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atlantic, pacific = set(), set()

        def dfs(r: int, c: int, seen: Set[Tuple[int, int]]) -> None:
            seen.add((r, c))
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, seen)

        for i in range(ROWS):
            dfs(i, 0, pacific)
        for j in range(COLS):
            dfs(0, j, pacific)
        
        for i in range(ROWS):
            dfs(i, COLS - 1, atlantic)
        for j in range(COLS):
            dfs(ROWS - 1, j, atlantic)

        return [list(cell) for cell in (atlantic & pacific)]