class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)
        
        topSort = []
        visited = set()
        path = set()

        def dfs(course) -> bool:
            if course in path: return False
            if course in visited: return True

            visited.add(course)
            path.add(course)
            for subsequent in adj[course]:
                if not dfs(subsequent): return False
            path.remove(course)
            topSort.append(course)
            return True
        
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course): return False
        
        return True if len(topSort) == numCourses else False