class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            L = dfs(node.left)
            R = dfs(node.right)
            if L is False or R is False or abs(L - R) > 1:
                return False
            return max(L, R) + 1
        res = dfs(root)
        return res is not False