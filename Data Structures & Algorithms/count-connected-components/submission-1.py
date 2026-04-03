class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [0] * n

        def _find(n: int) -> int:
            if par[n] != n:
                par[n] = _find(par[n])
            return par[n]
        
        def _union(pv: int, pe: int) -> bool:
            if pv == pe:
                return True
            if rank[pv] > rank[pe]:
                par[pe] = pv
            elif rank[pe] > rank[pv]:
                par[pv] = pe
            else:
                par[pe] = pv
                rank[pv] += 1
            return True

        for v, e in edges:
            pv, pe = _find(v), _find(e)
            _union(pv, pe)
        
        count = 0
        components = set()
        for node in range(n):
            root = _find(node)
            if root not in components:
                count += 1
                components.add(root)

        return count