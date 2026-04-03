class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        prefixTrie = PrefixTrie(words) # Build the prefix trie with all the words
        output = set() # Containing found words

        # Backtracking approach    
        def dfs(row: int, col: int, currWord: List, currNode: PrefixNode) -> None:
            
            # First make sure in bounds
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return
            
            # Check it is nvisited board cell and valid prefix
            # We use "#" to avoid using separate visited set and mark board directly in-place
            ch = board[row][col]
            if ch == "#" or ch not in currNode.children:
                return  
            
            child = currNode.children[ch] # Get new PrefixNode using current prefix
            currWord.append(ch) # Use a list as its mutable
            if child.word: # If we found the word in PrefixTrie
                output.add("".join(currWord)) # Convert list to a string and add to set
                child.word = False # Mark as false so that we can prune at the end

            board[row][col] = "#" # Mark cell as visited
            # visited.add((row, col)) 

            # Standard 2D grid backtracking
            dfs(row+1, col,   currWord, child)
            dfs(row,   col+1, currWord, child)
            dfs(row-1, col,   currWord, child)
            dfs(row,   col-1, currWord, child)
            
            # visited.remove((row,col)) 
            board[row][col] = ch # Unmark cell as visited, since we can reach from another potential path
            currWord.pop() # Remove from current word since we are done with this branch

            # Dead-end pruning
            if not child.children: # If its not a prefix for longer words
                del currNode.children[ch] # Then delete it so we dont traverse anymore

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, [], prefixTrie.root) # Backtrack at every cell since every cell could be start of word(s)
        
        return list(output) # Convert set back to a list


# Standard classes from NeetCode course

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