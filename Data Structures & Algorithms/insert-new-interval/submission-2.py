class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        def conflict(a, b):
            startA, endA = a
            startB, endB = b
            # Corrected logic: intervals overlap if max(starts) <= min(ends)
            return not (endA < startB or endB < startA)

        def merge(res):
            top = res.pop()
            second = res.pop()
            res.append([min(top[0], second[0]), max(top[1], second[1])])
                
        res = []
        # Sort intervals including the new one to handle insertion timing simply
        all_intervals = sorted(intervals + [newInterval])
        for i, (start, end) in enumerate(all_intervals):
            res.append([start, end])

            while len(res) > 1 and conflict(res[-1], res[-2]):
                merge(res)
        return res
