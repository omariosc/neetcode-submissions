class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = {}
        rank = {}

        def _find(n: int) -> int:
            if par[n] != n:
                par[n] = _find(par[n])
            return par[n]
        
        def _union(v: int, e: int) -> bool:
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
        
        def _check(n: int) -> int:
            if n not in par:
                par[n] = n
                rank[n] = 0
            return _find(n)
        
        for v, e in edges:
            pv, pe = _check(v), _check(e)
            _union(pv, pe)
        
        count = 0
        components = set()
        for n in par:
            root = _find(n)
            if root not in components:
                count += 1
                components.add(root)

        return count