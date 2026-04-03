class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # We want to sort edges, but need to return index within the edges set
        # So we append index to the list of edges
        for i in range(len(edges)):
            edges[i].append(i)
        
        # Sort edges by weight
        edges = sorted(edges, key=lambda x: x[2])

        # Get MST from all edges
        base = self.kruskal(n, edges)
        critical, pseudo = [], []

        for i, (u, v, w, idx) in enumerate(edges):
            # Test critical (skip edge)
            # If we skip and cost is higher, that edge was needed
            if self.kruskal(n, edges, skip=i) > base:
                critical.append(idx)
            else:
                # Test pseudo (force edge)
                # If we force the edge to be in MST and cost is same, edge was not needed
                # Note that it can never be lower because base IS the MST
                if self.kruskal(n, edges, force=i) == base:
                    pseudo.append(idx)

        return [critical, pseudo]

    # Standard Union Find
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Always Union, no need for rank
    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb: 
            return False
        self.parent[pb] = pa
        return True

    # Could have used Prim's too to create MST
    def kruskal(self, n, edges, skip=-1, force=-1):
        # Initialise parents for union find
        self.parent = list(range(n))
        # Total cost of MST and number of edges
        weight = count = 0

        # If we forced an edge
        if force != -1:
            u, v, w, _ = edges[force]
            # Union together, update min cost and number of edges
            self.union(u, v)
            weight = w
            count = 1

        for i, (u, v, w, _) in enumerate(edges):
            if i == skip:
                continue

            if self.union(u, v):
                weight += w
                count += 1

            if count == n - 1:
                break

        if count != n - 1:
            return float('inf')

        return weight