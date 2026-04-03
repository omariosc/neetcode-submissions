class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []          # Monotonic decreasing stack (stores indices)
        water = 0           # Total trapped water

        # Iterate through each bar
        for i in range(len(height)):

            # While:
            # 1. There is a previous bar
            # 2. Current bar is taller than the bar at stack top
            # This means we found a right wall that can trap water
            while stack and height[i] > height[stack[-1]]:

                bottom = stack.pop()  
                # This is the valley bottom between two walls

                # If stack becomes empty, there is no left wall
                # So no container can be formed
                if not stack:
                    break

                # Now:
                # stack[-1] = left wall index
                # i         = right wall index
                # bottom    = valley index

                # Width between the left and right walls
                distance = i - stack[-1] - 1

                # Height of trapped water is limited by
                # the shorter of the two walls
                bounded_height = (
                    min(height[i], height[stack[-1]]) 
                    - height[bottom]
                )

                # Add area (width × height)
                water += distance * bounded_height

            # Push current index onto stack
            # Maintains decreasing height order
            stack.append(i)

        return water