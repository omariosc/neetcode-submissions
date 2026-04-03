
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # We want to return the lowest common ancestor
        # Without lack of generality, if p.val >= q.val, 
        # swap p and q such that p.val <= q.val
        # Now p is in the left part of q 
        # if p.val <= root.val <= q.val return root
        # if root.val > q.val, we can prune the rightmost part --> go left
        # if root.val < p.val --> go right

        # Ensure p.val <= q.val
        if p.val > q.val:
            p, q = q, p

        # Base case
        if root is None:
            return None

        # If root is between p and q (inclusive), it's the LCA
        if p.val <= root.val <= q.val:
            return root

        # If both nodes are smaller, go left
        if root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # If both nodes are larger, go right
        if root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        