# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node: TreeNode, x: int):
            if not node:
                return 0
            good = 1 if node.val >= x else 0
            newX = max(node.val, x)
            return good + dfs(node.left, newX) + dfs(node.right, newX)

        return dfs(root, root.val)