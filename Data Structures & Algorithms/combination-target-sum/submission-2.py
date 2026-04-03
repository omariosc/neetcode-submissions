class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        length = len(nums)

        def findCombinations(idx: int, current: List[int], total: int) -> None:
            if total == target:
                combinations.append(current.copy())
                return
            if total > target:
                return
            
            for j in range(idx, length):
                current.append(nums[j])
                findCombinations(j, current, total + nums[j])
                current.pop()


        findCombinations(0, [], 0)
        return combinations