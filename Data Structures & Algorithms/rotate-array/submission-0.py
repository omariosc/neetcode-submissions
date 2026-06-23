class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        r = n - 1
        k %= n

        def reverse(L: int, R: int) -> None:
            while L < R:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
                R -= 1

        reverse(0, r)
        reverse(0, k - 1)
        reverse(k, n-1)