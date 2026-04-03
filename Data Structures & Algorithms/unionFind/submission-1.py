class UnionFind:
    
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.count = n

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.rank[px] > self.rank[py]:
            self.par[py] = px
        elif self.rank[px] < self.rank[py]:
            self.par[px] = py
        else:
            self.par[px] = py
            self.rank[py] += 1

        self.count -= 1
        return True

    def getNumComponents(self) -> int:
        return self.count
