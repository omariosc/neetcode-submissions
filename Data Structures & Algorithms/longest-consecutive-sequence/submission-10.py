class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        par = {}
        rank = {}
        num_set = set(nums)
            
        def _find(n):
            if par[n] != n:
                par[n] = _find(par[n])
            return par[n]

        def _union(a, b):
            pa, pb = _find(a), _find(b)
            if pa == pb:
                return False
            
            if rank[pa] >= rank[pb]:
                par[pb] = pa
                rank[pa] += rank[pb]
            else:
                par[pa] = pb
                rank[pb] += rank[pa]
            return True

        for n in num_set:
            par[n] = n
            rank[n] = 1
        
        for n in num_set:
            if (n-1) in par:
                _union(n, n-1)

        return max(rank.values())
