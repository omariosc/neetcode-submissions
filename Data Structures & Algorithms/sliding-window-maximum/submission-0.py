import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        L, R = 0, k - 1
        pq = nums[L:R+1]
        heapq._heapify_max(pq)
        freq = Counter(nums[L:R+1])

        for L in range(len(nums) - k + 1):
            while pq and freq[pq[0]] == 0:
                heapq._heappop_max(pq)
            res.append(pq[0])

            freq[nums[L]] -= 1
            if L + k < len(nums):
                val_in = nums[L + k]
                freq[val_in] += 1
                heapq._heappush_max(pq, val_in)
        return res
            