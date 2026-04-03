# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.preOrderTraversal(root, targetSum, 0)
 
    def preOrderTraversal(self, root, targetSum, currentSum):
        currentSum += root.val
        if targetSum == currentSum and not root.left and not root.right:
            return True
        if root.left and self.preOrderTraversal(root.left, targetSum, currentSum):
            return True
        if root.right and self.preOrderTraversal(root.right, targetSum, currentSum):
            return True
        return False