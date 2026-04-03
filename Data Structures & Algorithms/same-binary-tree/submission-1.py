class Solution:
    def isSameTree(self, p, q):

        def tree_hash(node):
            if node is None:
                return hash("null")

            left = tree_hash(node.left)
            right = tree_hash(node.right)

            return hash((node.val, left, right))

        return tree_hash(p) == tree_hash(q)