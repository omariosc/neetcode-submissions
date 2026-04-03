# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = (root, False)
        stack = [curr]
        while stack:
            curr, visited = stack.pop()
            if visited:
                if curr: res.append(curr.val)
            else:
                stack.append((curr, True))
                if curr and curr.right: stack.append((curr.right, False))
                if curr and curr.left: stack.append((curr.left, False))
        return res