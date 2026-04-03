class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(curr: List[int], used: Set[int]) -> List[List[int]]:
            if len(curr) == len(nums):
                if curr not in res:
                    res.append(curr.copy())
                return

            for i, n in enumerate(nums):
                if i not in used:
                    curr.append(n)
                    used.add(i)
                    helper(curr, used)
                    used.remove(i)
                    curr.pop()

        helper([], set())
        return res