class Solution:
    def trap(self, height: List[int]) -> int:


        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        trapped_water = 0

        while left < right:
            # Always process the side with the shorter boundary
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]  # Found a new tall wall
                else:
                    trapped_water += leftMax - height[left]  # Water trapped!
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]  # Found a new tall wall
                else:
                    trapped_water += rightMax - height[right]  # Water trapped!
                right -= 1

        return trapped_water
