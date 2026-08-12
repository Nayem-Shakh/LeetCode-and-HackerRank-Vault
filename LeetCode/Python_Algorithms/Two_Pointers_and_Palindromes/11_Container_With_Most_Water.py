"""
Problem: 11. Container With Most Water
Approach: Two-pointer technique starting from the outermost edges. Greedily calculates the area and shrinks the window by moving the pointer with the shorter height to maximize potential capacity.

Time Complexity: O(N) where N is the number of lines.
Space Complexity: O(1)
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            current_area = min(height[l], height[r]) * (r - l)
            max_area = max(current_area, max_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_area