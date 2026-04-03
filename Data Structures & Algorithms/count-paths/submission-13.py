class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        q = collections.deque()
        q.append((0,0))
        paths = 0
        while q:
            r, c = q.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                paths += 1
                continue
            if r + 1 < ROWS:
                q.append((r+1,c))
            if c + 1 < COLS:
                q.append((r,c+1))
        return paths