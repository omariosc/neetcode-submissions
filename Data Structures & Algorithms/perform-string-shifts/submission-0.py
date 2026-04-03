class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        queue = collections.deque(s)

        for direction, amount in shift:
            while amount:
                if direction == 1: queue.appendleft(queue.pop())
                else: queue.append(queue.popleft())
                amount -= 1
        
        return "".join(queue)