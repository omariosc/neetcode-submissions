class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        names = {}
        for account in accounts:
            for email in account[1:]:
                names[email] = account[0]

        par = {}
        rank = {}

        def _find(x: str) -> str:
            if par[x] != x:
                par[x] = _find(par[x])
            return par[x]
        
        def _union(px: str, py: str) -> None:
            if px != py:
                if rank[px] < rank[py]:
                    par[px] = py
                elif rank[py] < rank[px]:
                    par[py] = px
                else:
                    par[px] = py
                    rank[py] += 1

        def _check(e: str) -> None:
            if e not in par:
                par[e] = e
                rank[e] = 0
            
        for account in accounts:
            first = account[1]
            _check(first)
            for email in account[2:]:
                _check(email)                
                _union(_find(first), _find(email))

        groups = collections.defaultdict(list)
        for email in par:
            root = _find(email)
            groups[root].append(email)
    
        res = []
        for root, emails in groups.items():
            res.append([names[root]] + sorted(emails))
        return res
