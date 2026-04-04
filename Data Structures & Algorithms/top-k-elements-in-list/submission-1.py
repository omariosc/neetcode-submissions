class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()

        tmp_stack = []
        max_stack = []

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 0
            freq[nums[i]] += 1

            while len(max_stack) > 0 and freq[nums[i]] > max_stack[-1][1]:
                top = max_stack.pop()
                tmp_stack.append(top)
            max_stack.append((nums[i],freq[nums[i]]))
            if len(tmp_stack) > 0:
                while len(max_stack) < k:
                    max_stack.append(tmp_stack.pop())
                tmp_stack = []

        return [x[0] for x in max_stack]