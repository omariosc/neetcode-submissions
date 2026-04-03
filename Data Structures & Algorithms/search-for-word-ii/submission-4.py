class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        prefixTrie = PrefixTrie(words) # Build the prefix trie with all the words
        output = set() # Containing found words
        visited = set() # Visited cells in board

        # Backtracking approach    
        def dfs(row: int, col: int, 
                currWord: List, currNode: PrefixNode) -> None:
            # Make sure in bounds, unvisited board cell and valid prefix
            if (row < 0 or col < 0 or 
                row >= len(board) or col >= len(board[0]) or 
                (row, col) in visited or 
                board[row][col] not in currNode.children):
                return  
            
            
            child = currNode.children[board[row][col]] # Get new PrefixNode using current prefix
            currWord.append(board[row][col]) # Use a list as its mutable
            if child.word: # If we found the word in PrefixTrie
                output.add("".join(currWord)) # Convert list to a string and add to set
                child.word = False # Mark as false so that we can prune at the end

            visited.add((row, col)) # Mark cell as visited

            # Standard 2D grid backtracking
            dfs(row+1, col,   currWord, child)
            dfs(row,   col+1, currWord, child)
            dfs(row-1, col,   currWord, child)
            dfs(row,   col-1, currWord, child)
            
            visited.remove((row,col)) # Unmark cell as visited, since we can reach from another potential path
            currWord.pop() # Remove from current word since we are done with this branch

            # Dead-end pruning
            if not child.children: # If its not a prefix for longer words
                del currNode.children[board[row][col]] # Then delete it so we dont traverse anymore

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