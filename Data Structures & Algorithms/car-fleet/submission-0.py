class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - p) / s for p, s in cars]
        
        fleets = 0
        max_time = 0.0
        for t in times:
            if t > max_time:
                fleets += 1
                max_time = t
            
        return fleets