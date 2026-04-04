# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if not root.left or (root.left and root.left.val < root.val):
            left = self.isValidBST(root.left)
        else:
            return False
            
        if not root.right or (root.right and root.right.val > root.val):
            right = self.isValidBST(root.right)
        else:
            return False
        
        return left and right