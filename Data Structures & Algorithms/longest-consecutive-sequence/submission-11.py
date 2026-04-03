class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0 
        par = {} # Store the root of the consecutive sequence chain
        rank = {} # Store the length of connected chain
        num_set = set(nums) # We don't care about duplicates
            
        def _find(n): # Standard union find
            if par[n] != n:
                par[n] = _find(par[n])
            return par[n]

        def _union(a, b):
            pa, pb = _find(a), _find(b)
            if pa == pb:
                return False
            
            # Union by size instead of rank
            # We don't care about which of a or b is bigger, since parent 
            # will always store correct length for longest sequence
            if rank[pa] >= rank[pb]:
                par[pb] = pa
                rank[pa] += rank[pb]
            else:
                par[pa] = pb
                rank[pb] += rank[pa]
            return True

        # Initialise parents and ranks
        for n in num_set:
            par[n] = n
            rank[n] = 1
        
        # If we know that previous number exists
        # union to combine length of their respective longest sequences
        for n in num_set:
            if (n-1) in par:
                _union(n, n-1)

        # Gets the largest sequence
        return max(rank.values())
