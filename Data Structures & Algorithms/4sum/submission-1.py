class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums)):
                b = nums[j]
                if j > i + 1 and b == nums[j-1]:
                    continue

                L, R = j + 1, n - 1
                while L < R:
                    fourSum = a + b + nums[L] + nums[R]
                    if fourSum < target: 
                        L += 1
                    elif fourSum > target:
                        R -= 1
                    else:
                        res.add((a,b,nums[L],nums[R]))
                        L += 1
                        R -= 1
        unique = []
        for comb in res:
            unique.append(list(comb))
        return unique
