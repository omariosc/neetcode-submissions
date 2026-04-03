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
        n = [(self.root, 0)]
        while n:
            curr, i = n.pop()
            if i == len(word):
                if curr.word:
                    return True
                continue
            ch = word[i]
            if ch == ".":
                n += [(c, i+1) for c in curr.children.values()]
                continue
            if ch in curr.children:
                n.append((curr.children[ch], i+1))
        return False

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False