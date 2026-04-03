class Solution:   

    def inOrder(self, root):
        if not root:
            return "$"
        return str(root.val) + self.inOrder(root.left) + self.inOrder(root.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        substring = self.inOrder(subRoot)
        string = self.inOrder(root)

        return substring in string