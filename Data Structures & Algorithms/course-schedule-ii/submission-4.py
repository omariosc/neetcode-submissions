class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        topSort, visited, path = [], set(), set()

        def dfs(course):
            if course in path: return False
            if course in visited: return True

            path.add(course)
            for neighbour in graph[course]:
                if not dfs(neighbour): return False
            path.remove(course)
            visited.add(course)
            topSort.append(course)
            return True
        
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course): return []
                
        return topSort[::-1] if numCourses == len(topSort) else []