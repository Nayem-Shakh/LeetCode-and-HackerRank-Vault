"""
Problem: 217. Contains Duplicate
Approach: Utilized a Hash Set for O(1) lookups to track unique elements, avoiding O(N^2) nested loops.

Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums: 
            if num in seen:
                return True
            seen.add(num)
        return False
