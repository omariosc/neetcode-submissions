class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {}
        rank = {}
        cycle = []

        # Standard UnionFind
        def _findParent(n):
            if par[n] != n:
                par[n] = _findParent(par[n])
            return par[n]

        for v, e in edges:
            # Since we don't know of nodes beforehand, assume its first time we are seeing them
            pv, pe = v, e 

            if v not in par: # If its a new node
                par[v] = v
            else:
                pv = _findParent(v) # Standard UnionFind
                
            if e not in par: # If its a new node
                par[e] = e
            else:
                pe = _findParent(e) # Standard UnionFind
            
            if pv == pe:
                cycle = [v, e] # Will automatically update the latest cycle you have found
                continue
            
            # Neat trick to set rank to 0 if doesn't exist, otherwise get rank of v's parent
            rpv = rank.setdefault(pv, 0) 
            rpe = rank.setdefault(pe, 0)

            if rpv < rpe:
                par[pv] = pe
            elif rpv > rpe:
                par[pe] = pv
            else:
                par[pv] = pe
                rank[pe] += 1

        return cycle # Guarantee that most recent edge we can remove was in `cycle`