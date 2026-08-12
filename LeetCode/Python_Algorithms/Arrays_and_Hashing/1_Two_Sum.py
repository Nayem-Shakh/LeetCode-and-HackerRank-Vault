"""
Problem: 1. Two Sum
Approach: Single-pass Hash Map. Stores the complement of each number and its index, allowing for an O(1) lookup as the array is traversed.

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        
        return []
