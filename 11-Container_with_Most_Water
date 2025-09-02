from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the current area
            current_area = min(height[left], height[right]) * (right - left)

            # Update the max area if the current area is larger
            max_area = max(max_area, current_area)

            # Move the pointer of the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area