# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        def dfs(node):
            if not node:
                return 0
            L = dfs(node.left)
            R = dfs(node.right)
            height = 1 + max(L, R)
            self.maxDiameter = max(self.maxDiameter, L + R)
            return height

        dfs(root)
        return self.maxDiameter