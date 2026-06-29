from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        values = self.keys[key]
        idx = bisect.bisect_right(values, [timestamp, chr(127)])
        return values[idx - 1][1] if idx > 0 else ""
        # start, end = 0, len(values) - 1
        # while start <= end:
        #     mid = (start + end) // 2
        #     if timestamp < values[mid][0]:
        #         end = mid - 1
        #     elif timestamp > values[mid][0]:
        #         start = mid + 1
        #     else:
        #         return values[mid][1]
        # return values[end][1] if end >= 0 else ""
