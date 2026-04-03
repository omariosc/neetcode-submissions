class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Store the name per email for all accounts at the beginning - O(n)
        names = {}
        for account in accounts:
            for email in account[1:]:
                names[email] = account[0]

        # Initialise parents and ranks for union find
        par = {}
        rank = {}

        # Could have made a class and Union Find object like in NeetCode's solution - O(1)
        def _find(x: str) -> str:
            # I prefer recursive find over the while loop
            if par[x] != x:
                par[x] = _find(par[x])
            return par[x]
        
        # We get parents laters on but could do it here too - O(1)
        def _union(px: str, py: str) -> None:
            if px != py:
                if rank[px] < rank[py]:
                    par[px] = py
                elif rank[py] < rank[px]:
                    par[py] = px
                else:
                    par[px] = py
                    rank[py] += 1

        # Helper function to initialise parent and rank for unseen emails - O(1)
        def _check(e: str) -> None:
            if e not in par:
                par[e] = e
                rank[e] = 0
            
        # Go over all accounts - O(n)
        for account in accounts:
            # We union all emails with the first one
            first = account[1]
            _check(first)
            # Iterating from the second email onwards (if exists)
            for email in account[2:]:
                _check(email)                
                _union(_find(first), _find(email))

        # Now process the parents by finding root of each email - O(n)
        groups = collections.defaultdict(list)
        for email in par:
            root = _find(email)
            # Group these emails under the root email (technically this was picked arbitrarily)
            groups[root].append(email)
    
        # We now go through all the roots - O(nlogn)
        res = []
        for root, emails in groups.items():
            # Our pre-processed names comes in handy here!
            res.append([names[root]] + sorted(emails))
        return res