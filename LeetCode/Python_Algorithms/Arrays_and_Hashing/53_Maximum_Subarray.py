"""
Problem: 53. Maximum Subarray
Approach: Kadane's Algorithm. Tracks the maximum contiguous sum ending at the current position and updates the global maximum.

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = nums[0]
        max_so_far = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_so_far = max(current_sum, max_so_far)
            
        return max_so_far
