class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cp = [1] * n
        for _ in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                cp[c] += cp[c+1]
        return cp[0]