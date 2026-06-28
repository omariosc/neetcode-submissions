class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def helper(node, allowed):
            if not node:
                return 0
            state = (node, allowed)
            if state in memo:
                return memo[state]
            
            # Option 1: Always allowed to skip the current node
            leftSkip = helper(node.left, True)
            rightSkip = helper(node.right, True)
            skip = leftSkip + rightSkip

            # Option 2: Rob the current node only if allowed
            rob = 0
            if allowed:
                leftRob = helper(node.left, False)
                rightRob = helper(node.right, False)
                rob = node.val + leftRob + rightRob

            res = max(rob, skip)
            memo[state] = res
            return res
        
        return helper(root, True)