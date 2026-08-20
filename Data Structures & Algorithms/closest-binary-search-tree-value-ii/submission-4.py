from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        self.values = deque()
        
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            
            if len(self.values) < k:
                self.values.append(node.val)
            else:
                if abs(node.val - target) < abs(self.values[0] - target):   
                    self.values.popleft()
                    self.values.append(node.val)

            dfs(node.right)
        
        dfs(root)
        return list(self.values)