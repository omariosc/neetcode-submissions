import hashlib
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def merkle(node):
            if not node:
                return "null"
            
            left_hash = merkle(node.left)
            right_hash = merkle(node.right)

            # Simple idea - convert this to some bytes
            data = f"{node.val}-{left_hash}-{right_hash}".encode()
            
            # Use SHA256 hashing algorithm to convert those bytes into 256 hashed bytes.
            # hexdigest converts these bytes into hex
            node_hash = hashlib.sha256(data).hexdigest()
            
            # Create a new attribute for the node's hash
            node.hash = node_hash

            return node_hash
        
        merkle(root) # We need to produce hashes for every node in the root tree
        subRootHash = merkle(subRoot) # Same for sub root, but lets also store the final hash to compare with
        self.state = False # We let dfs update this if the hash ever matched

        def dfs(node):
            if node:
                if node.hash == subRootHash:
                    self.state = True
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        
        return self.state           
