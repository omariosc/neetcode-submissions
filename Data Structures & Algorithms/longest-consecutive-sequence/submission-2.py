class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
            
        consecutive_lists = dict()
        max_length = 1

        nums = set(sorted(nums))

        for i in nums:
            if i in consecutive_lists:
                consecutive_lists[i].append(i)
                consecutive_lists[i+1] = consecutive_lists.pop(i)
                if len(consecutive_lists[i+1]) > max_length:
                    max_length = len(consecutive_lists[i+1])
            else:
                consecutive_lists[i+1] = [i]

        return max_length