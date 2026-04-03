class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        Solution.produceCombinations(1, [], combinations, n, k)
        return combinations
    
    @staticmethod
    def produceCombinations(i: int, current: List[int], combinations: List[List[int]], n: int, k: int) -> None:
        if len(current) == k:
            combinations.append(current.copy())
            return
        if i > n:
            return
        
        current.append(i)
        Solution.produceCombinations(i+1, current, combinations, n, k)
        current.pop()
        Solution.produceCombinations(i+1, current, combinations, n, k)