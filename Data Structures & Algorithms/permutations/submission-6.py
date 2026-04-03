class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(curr: List[int], used: Set[int]) -> List[List[int]]:
            if len(curr) == len(nums):
                res.append(curr.copy())

            for n in nums:
                if n not in used:
                    curr.append(n)
                    used.add(n)
                    helper(curr, used)
                    used.remove(n)
                    curr.pop()

        helper([], set())
        return res