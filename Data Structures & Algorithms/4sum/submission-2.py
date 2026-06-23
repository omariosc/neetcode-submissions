class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Smallest possible sum with nums[i]
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break

            # Largest possible sum with nums[i]
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Smallest possible sum with nums[i], nums[j]
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break

                # Largest possible sum with nums[i], nums[j]
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue

                L, R = j + 1, n - 1

                while L < R:
                    total = nums[i] + nums[j] + nums[L] + nums[R]

                    if total < target:
                        L += 1
                    elif total > target:
                        R -= 1
                    else:
                        res.append([nums[i], nums[j], nums[L], nums[R]])

                        L += 1
                        R -= 1

                        while L < R and nums[L] == nums[L - 1]:
                            L += 1

                        while L < R and nums[R] == nums[R + 1]:
                            R -= 1

        return res