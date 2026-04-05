class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        letters = set("".join(words))

        adjList = {letter: set() for letter in letters}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjList[w1[j]].add(w2[j])
                    break

        topSort, visited = [], {} # False = visiting, True = visited
        def dfs(letter):
            if letter in visited:
                return visited[letter]
            
            visited[letter] = False
            for neighbour in adjList[letter]:
                if not dfs(neighbour):
                    return False
            
            visited[letter] = True
            topSort.append(letter)
            return True

        for letter in sorted(adjList.keys(), reverse=True):
            if not dfs(letter):
                return ""

        return "".join(topSort[::-1])