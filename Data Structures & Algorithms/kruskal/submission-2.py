class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        pq = []
        for u, v, w in edges:
            heapq.heappush(pq, (w, u, v))
        
        UF = UnionFind(n)
        e = c = 0
        while e < n - 1 and pq:
            w, u, v = heapq.heappop(pq)
            if UF.union(u, v):
                c += w
                e += 1
        
        return c if e == n-1 else -1

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
    
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, a, b):
        pA, pB = self.find(a), self.find(b)
        if pA == pB:
            return False
        self.par[pA] = pB
        return True
