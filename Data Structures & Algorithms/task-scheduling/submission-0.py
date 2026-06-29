class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for t in tasks:
            freq[ord(t) - ord('A')] += 1

        counts = []
        for f in freq:
            if f > 0:
                counts.append(f)
        counts.sort(reverse=True)
        
        max_f = counts[0]
        max_f_count = counts.count(max_f)
        
        res = (max_f - 1) * (n + 1) + max_f_count
        return max(res, len(tasks))