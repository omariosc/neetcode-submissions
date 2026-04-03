class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        prefixTrie = PrefixTrie(words)
        cache = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self._dfs(board, i, j, [], prefixTrie.root, set(), cache, prefixTrie)
        return list(cache)

    def _dfs(self, board: List[List[str]], row: int, col: int, currWord: List, currNode: PrefixNode, visited: Set[Tuple], cache: Set[str], prefixTrie: PrefixTrie) -> None:
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or (row, col) in visited:
            return  
        
        ch = board[row][col]
        if ch not in currNode.children:
            return
        currNode = currNode.children[ch]
        currWord.append(ch)
        if currNode.word:
            cache.add("".join(currWord))

        visited.add((row, col))
        self._dfs(board, row+1, col,   currWord, currNode, visited, cache, prefixTrie)
        self._dfs(board, row,   col+1, currWord, currNode, visited, cache, prefixTrie)
        self._dfs(board, row-1, col,   currWord, currNode, visited, cache, prefixTrie)
        self._dfs(board, row,   col-1, currWord, currNode, visited, cache, prefixTrie)
        visited.remove((row,col))
        currWord.pop()

class PrefixTrie:
    def __init__(self, words: List[str]):
        self.root = PrefixNode()
        for word in words:
            self.insert(word)

    def insert(self, word: List) -> None:
        n = self.root
        for char in word:
            if char not in n.children:
                n.children[char] = PrefixNode()
            n = n.children[char]
        n.word = True


class PrefixNode:
    def __init__(self):
        self.children = {}
        self.word = False