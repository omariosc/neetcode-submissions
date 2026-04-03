class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        prefixTrie = PrefixTrie(words)
        output = visited = set()

        def dfs(row: int, col: int, 
                currWord: List, currNode: PrefixNode) -> None:
            if (row < 0 or col < 0 or 
                row >= len(board) or col >= len(board[0]) or 
                (row, col) in visited or 
                board[row][col] not in currNode.children):
                return  
            
            currNode = currNode.children[board[row][col]]
            currWord.append(board[row][col])
            if currNode.word:
                output.add("".join(currWord))

            visited.add((row, col))
            dfs(row+1, col,   currWord, currNode)
            dfs(row,   col+1, currWord, currNode)
            dfs(row-1, col,   currWord, currNode)
            dfs(row,   col-1, currWord, currNode)
            visited.remove((row,col))
            currWord.pop()

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, [], prefixTrie.root)
        
        return list(output)


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