"""
Problem: 169. Majority Element
Approach: Boyer-Moore Voting Algorithm. Maintains a candidate and a counter to find the majority element in a single pass without requiring extra memory.

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate
