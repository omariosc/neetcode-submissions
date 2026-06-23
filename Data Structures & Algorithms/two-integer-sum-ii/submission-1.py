class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(x: int, L: int, R: int) -> int:
            while L <= R:
                M = (L+R)//2
                if M >= len(numbers):
                    break
                if x < numbers[M]:
                    R = M - 1
                elif x > numbers[M]:
                    L = M + 1
                else:
                    return M
            return -1
        for i, n in enumerate(numbers):
            t = binary_search(target - n, i + 1, len(numbers) - 1)
            if t != -1:
                return [i+1, t+1]
