class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = SegmentTree.build(nums, 0, len(nums) - 1)
    
    @staticmethod
    def build(nums: List[int], L: int, R: int) -> 'Node':
        if L == R:
            return Node(nums[L], L, L)

        M = L + (R - L) // 2
        root = Node(0, L, R)
        root.left = SegmentTree.build(nums, L, M)
        root.right = SegmentTree.build(nums, M+1, R)
        root.total = root.left.total + root.right.total
        return root
    
    def update(self, index: int, val: int) -> None:
        SegmentTree.updateNode(self.root, index, val)

    @staticmethod
    def updateNode(node: 'Node', index: int, val: int) -> None:
        if node.L == node.R:
            node.total = val
            return

        M = node.L + (node.R - node.L) // 2
        if index > M:
            SegmentTree.updateNode(node.right, index, val)
        else:
            SegmentTree.updateNode(node.left, index, val)
        node.total = node.left.total + node.right.total

    def query(self, L: int, R: int) -> int:
        return SegmentTree.queryRange(self.root, L, R)
    
    @staticmethod
    def queryRange(node: 'Node', L: int, R: int) -> int:
        if L <= node.L and node.R <= R:
            return node.total
        
        if node.R < L or R < node.L:
            return 0

        return SegmentTree.queryRange(node.left, L, R) + SegmentTree.queryRange(node.right, L, R)

class Node:
    def __init__(self, val: int, L: int, R: int):
        self.total = val
        self.left = None
        self.right = None
        self.L = L
        self.R = R
