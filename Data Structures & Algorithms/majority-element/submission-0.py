class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        max_n = nums[0]
        for n in nums:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1
            if counter[n] > counter[max_n]:
                max_n = n
        return max_n