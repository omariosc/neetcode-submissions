class Solution:
    def __init__(self):
        self.count = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.dfs(root, k)

    def dfs(self, root, k):
        if not root:
            return
        
        left = self.dfs(root.left, k)
        if left is not None:
            return left
            
        self.count += 1
        if k == self.count:
            return root.val
            
        return self.dfs(root.right, k)