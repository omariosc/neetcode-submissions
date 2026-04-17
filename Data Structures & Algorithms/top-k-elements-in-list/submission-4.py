class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0)+ 1

        # for n in nums:
        #     freq[n] = freq.get(n, 0) + 1

        sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        return [num for num, _ in sorted_items[:k]]