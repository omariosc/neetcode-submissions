# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.iterator = self.dfs(root)
        self._next = next(self.iterator, None)

    def dfs(self, node):
        if node:  
            yield from self.dfs(node.left)
            yield node.val
            yield from self.dfs(node.right)

    def next(self):
        val = self._next
        self._next = next(self.iterator, None)
        return val

    def hasNext(self):
        return self._next is not None
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()