class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # Initialise min heap
        pq = []
        for u, v, w in edges:
            heapq.heappush(pq, (w, u, v))
        
        # Using union find
        UF = UnionFind(n)

        # Initialise number of edges found and min cost
        e = c = 0

        # As long as we need more edges, and have edges to look through
        while e < n - 1 and pq:
            w, u, v = heapq.heappop(pq)
            # If we can union, increment number of edges and update min cost
            if UF.union(u, v):
                c += w
                e += 1
        
        # Make sure all vertices are connected
        return c if e == n-1 else -1

class UnionFind:
    def __init__(self, n):
        # No need for rank
        self.par = [i for i in range(n)]
    
    def find(self, x):
        # Standard union find 
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, a, b):
        pA, pB = self.find(a), self.find(b)
        if pA == pB:
            return False
        # Always union, does not matter which is parent
        self.par[pA] = pB
        return True
