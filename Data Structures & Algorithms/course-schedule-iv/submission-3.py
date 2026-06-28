class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        is_prereq = [[False] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            is_prereq[u][v] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                if not is_prereq[i][k]:
                    continue
                for j in range(numCourses):
                    if is_prereq[k][j]:
                        is_prereq[i][j] = True

        return [is_prereq[u][v] for u, v in queries]
        
        # res = []
        # for u, v in queries:
        #     res.append(is_prereq[u][v])
        # return res