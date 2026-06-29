class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []

        def produceCombinations(curr: List[int], i: int):
            if sum(curr) == target:
                self.res.append(curr.copy())
                return
            elif i == len(candidates) or sum(curr) > target:
                return 0

            curr.append(candidates[i])
            produceCombinations(curr, i+1)
            curr.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            produceCombinations(curr, i+1)

        produceCombinations([], 0)
        return self.res