class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {}
        rank = {}
        cycle = []

        def _findParent(n):
            if par[n] != n:
                par[n] = _findParent(par[n])
            return par[n]

        for v, e in edges:
            pv, pe = v, e

            if v not in par:
                par[v] = v
            else:
                pv = _findParent(v)
            if e not in par:
                par[e] = e
            else:
                pe = _findParent(e)
            
            if pv == pe:
                cycle = [v, e]
                continue
            
            rpv = rank.setdefault(pv, 0)
            rpe = rank.setdefault(pe, 0)
            if rpv < rpe:
                par[pv] = pe
            elif rpv > rpe:
                par[pe] = pv
            else:
                par[pv] = pe
                rank[pe] += 1

        return cycle