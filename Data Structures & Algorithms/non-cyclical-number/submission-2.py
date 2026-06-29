class Solution:
    def isHappy(self, n: int) -> bool:
        def nextHappy(x: str) -> int:
            h = 0
            for i in x:
                h += int(i)**2
            return h

        slow = n
        fast = nextHappy(str(n))
        while slow != fast and slow != 1:
            slow = nextHappy(str(slow))
            fast = nextHappy(str(nextHappy(str(fast))))
        if slow == 1: return True
        return False
