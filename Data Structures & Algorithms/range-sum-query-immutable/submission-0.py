class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = []
        total = 0
        for n in nums:
            total += n
            self.sums.append(total)

    def sumRange(self, left: int, right: int) -> int:
        sumsRight = self.sums[right]
        sumsLeft = self.sums[left - 1] if left > 0 else 0
        return sumsRight - sumsLeft


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)