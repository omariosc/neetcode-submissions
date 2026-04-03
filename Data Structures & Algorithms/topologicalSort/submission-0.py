class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        
        topSort = []
        visited, path = set(), set()

        def dfs(i: int) -> bool:
            if i in path:
                return False
            if i in visited:
                return True
            
            visited.add(i)
            path.add(i)
            for neighbour in adj[i]:
                if not dfs(neighbour): return False
            path.remove(i)
            topSort.append(i)
            return True

        for i in range(n):
            if i not in visited:
                if not dfs(i): return []

        return topSort[::-1]