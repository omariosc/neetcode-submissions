class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        topSort = []
        visited, path = set(), set()

        def dfs(node: int) -> bool:
            if node in path:
                return False
            if node in visited:
                return True
            
            visited.add(node)
            path.add(node)

            for neighbour in adj[node]:
                if not dfs(neighbour): return False
            path.remove(node)
            topSort.append(node)
            return True
        
        for node in range(n):
            if node not in visited:
                if not dfs(node): return []
        
        return topSort[::-1]
