class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        n = self.root
        for c in word:
            if c not in n.children:
                n.children[c] = TrieNode()
            n = n.children[c]
        n.word = True
    
    def search(self, word: str) -> bool:
        return self._dfs(word, 0, self.root)
        
    def _dfs(self, word: str, i: int, node: TrieNode) -> bool:
        if i == len(word):
            return node.word

        c = word[i]

        if c != ".":
            if c not in node.children:
                return False
            return self._dfs(word, i+1, node.children[c])
        else:
            for child in node.children.values():
                if self._dfs(word, i+1, child):
                    return True
            return False

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False