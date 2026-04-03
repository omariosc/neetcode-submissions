class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = [([], set())]

        while stack:
            path, used = stack.pop()

            if len(path) == len(nums):
                res.append(path)
                continue

            for i, num in enumerate(nums):
                if i not in used:
                    new_path = path + [num]
                    new_used = used | {i}
                    stack.append((new_path, new_used))
        
        return res