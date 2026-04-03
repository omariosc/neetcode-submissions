class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    @staticmethod
    def build(nums, L: int, R: int) -> 'SegmentNode':
        if L == R:
            return SegmentNode(nums[L], L, R)
        
        M = L + (R - L) // 2
        root = SegmentNode(0, L, R)
        root.left = SegmentTree.build(nums, L, M)
        root.right = SegmentTree.build(nums, M+1, R)
        root.sum = root.left.sum + root.right.sum
        return root
    
    def update(self, index: int, val: int) -> None:
        self.updateNode(self.root, index, val)

    @staticmethod
    def updateNode(node: 'SegmentNode', index: int, val: int) -> None:
        if node.L == node.R:
            node.sum = val
            return
        
        M = node.L + (node.R - node.L) // 2
        if index > M:
            SegmentTree.updateNode(node.right, index, val)
        else: # index <= M
            SegmentTree.updateNode(node.left, index, val)
        node.sum = node.left.sum + node.right.sum
    
    def query(self, L: int, R: int) -> int:
        return self.queryRange(self.root, L, R)

    @staticmethod
    def queryRange(node: 'SegmentNode', L: int, R: int) -> int:
        if L <= node.L and node.R <= R:
            return node.sum

        M = node.L + (node.R - node.L) // 2
        if L > M:
            return SegmentTree.queryRange(node.right, L, R)
        elif R <= M:
            return SegmentTree.queryRange(node.left, L, R)
        else:
            return SegmentTree.queryRange(node.left, L, M) + SegmentTree.queryRange(node.right, M+1, R)

class SegmentNode:
    def __init__(self, value: int, L: int, R: int):
        self.sum = value
        self.left = None
        self.right = None
        self.L = L
        self.R = R