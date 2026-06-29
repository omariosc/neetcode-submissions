class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        def produceCombinations(curr: List[str], opens: int, closes: int):
            if opens == closes == n:
                self.res.append("".join(curr))
                return
            
            if opens < n:
                curr.append("(")
                produceCombinations(curr, opens + 1, closes)
                curr.pop()
            
            if closes < opens:
                curr.append(")")
                produceCombinations(curr, opens, closes + 1)
                curr.pop()

        produceCombinations([], 0, 0)
        return self.res