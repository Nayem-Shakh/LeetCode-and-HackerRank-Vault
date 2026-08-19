"""
Problem: 1764. Form Array by Concatenating Subarrays of Another Array
Approach: Greedy array slicing. Iterates through the nums array and checks if the current slice matches the targeted subarray from groups. If a match is found, it advances the index pointer by the length of the matched group to ensure the subarrays are non-overlapping and maintain their exact order.

Time Complexity: O(N \cdot K) where N is the length of nums and K is the maximum length of a subarray in groups (due to the list slicing and element comparison).
Space Complexity: O(K) because Python list slicing creates a temporary new list in memory.
"""
from typing import List

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        current = 0
        n = len(nums)
        i = 0

        while i < n:
            if nums[i:i+len(groups[current])] == groups[current]:
                i += len(groups[current])
                current += 1
                if current == len(groups):
                    return True
            else:
                i += 1
                
        return False