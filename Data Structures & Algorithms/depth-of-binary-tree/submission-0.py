# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def _dfs(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            
            return 1 + max(_dfs(root.left), _dfs(root.right))
        
        return _dfs(root)