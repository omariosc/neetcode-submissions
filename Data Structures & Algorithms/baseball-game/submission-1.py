class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for o in operations:
            if o == "+":
                score.append(score[-1] + score[-2])
            elif o == "D":
                score.append(score[-1] * 2)
            elif o == "C":
                score.pop()
            else:
                score.append(int(o))
        return sum(score)
