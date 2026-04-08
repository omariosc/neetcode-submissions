# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxSum = root.val

        def dfs(node):
            nonlocal maxSum

            if not node:
                return 0
            
            leftPathSum = dfs(node.left)
            rightPathSum = dfs(node.right)
            pathSum = node.val + max(max(0,leftPathSum), max(0,rightPathSum))
            chainSum = node.val + max(0, leftPathSum) + max(0, rightPathSum)
            maxSum = max(maxSum, pathSum, chainSum)
            return pathSum

        dfs(root)
        return maxSum