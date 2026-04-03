class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        q = collections.deque()
        visited = set()
        q.append((0,0))
        visited.add((0,0))
        paths = 0
        while q:
            r, c = q.popleft()
            visited.add((r,c))
            if r == ROWS - 1 and c == COLS - 1:
                paths += 1
                continue
            if r + 1 < ROWS and (r+1,c) not in visited:
                q.append((r+1,c))
            if c + 1 < COLS and (r,c+1) not in visited:
                q.append((r,c+1))
        return paths