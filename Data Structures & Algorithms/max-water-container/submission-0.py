class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = min(heights[0], heights[-1]) * (len(heights)-1)
        l = 0
        r = len(heights) - 1

        while l < r:
            c = min(heights[l], heights[r]) * (r-l)
            if c > m:
                m = c
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l, r = l + 1, r - 1

        return m