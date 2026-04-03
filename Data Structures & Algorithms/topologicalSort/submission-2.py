class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        topSort, visited, path = [], set(), set()
        for node in range(n):
            if node not in visited:
                if not self.dfs(node, visited, path, adj, topSort): return []
        
        return topSort[::-1]

    def dfs(self, node: int, visited: Set[int], path: Set[int], adj: Dict[int, List[int]], topSort: List[int]) -> bool:
        if node in path: return False
        if node in visited: return True

        visited.add(node)
        path.add(node)

        for neighbour in adj[node]:
            if not self.dfs(neighbour, visited, path, adj, topSort): return False
        
        path.remove(node)
        topSort.append(node)
        return True