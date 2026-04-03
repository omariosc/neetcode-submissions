class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def produceCombinations(i: int, curr: List[int]) -> None:
            nonlocal combinations, n, k
            if len(curr) == k:
                combinations.append(curr.copy())
                return
            if i > n:
                return
            
            for j in range(i, n+1):
                curr.append(j)
                produceCombinations(j+1, curr)
                curr.pop()

        produceCombinations(1, [])
        return combinations
