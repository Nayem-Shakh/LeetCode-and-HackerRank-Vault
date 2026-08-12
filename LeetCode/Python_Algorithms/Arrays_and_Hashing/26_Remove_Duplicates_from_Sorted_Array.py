"""
Problem: 26. Remove Duplicates from Sorted Array
Approach: In-place two-pointer technique. Since the array is sorted, duplicates are adjacent. The writer pointer only advances when a new unique element is found by the reader.

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        writer = 1

        for reader in range(1, len(nums)):
            if nums[reader] != nums[reader - 1]:
                nums[writer] = nums[reader]
                writer += 1
                
        return writer
