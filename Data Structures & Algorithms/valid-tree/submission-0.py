
class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]

    def find(self, p: int) -> int:
        if p != self.par[p]:
            self.par[p] = self.find(self.par[p])
        return self.par[p]

    def union(self, a: int, b: int) -> bool:
        parA, parB = self.find(a), self.find(b)
        if parA == parB:
            return False
        self.par[parA] = parB
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        UF = UnionFind(n)
        for u, v in edges:
            if not UF.union(u, v): 
                return False
        par = UF.find(0)
        for i in range(n):
            if UF.find(i) != par:
                return False
        return True