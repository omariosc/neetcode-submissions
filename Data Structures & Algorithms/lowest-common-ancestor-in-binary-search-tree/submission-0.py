# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node: TreeNode, val: int, path: List[int]) -> None:
            if not node:
                return
            if node.val == val:
                path += [node]
                return True
            
            path += [node]
            if dfs(node.left, val, path):
                return True
            elif dfs(node.right, val, path):
                return True
            path.pop()
            return False
        
        pathP = []
        dfs(root, p.val, pathP)

        pathQ = []
        dfs(root, q.val, pathQ)
        setQ = set(pathQ)

        for n in pathP:
            print(n.val)
        print()
        for n in pathQ:
            print(n.val)

        for i in range(len(pathP)-1, -1, -1):
            if pathP[i] in setQ:
                return pathP[i]        
