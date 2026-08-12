"""
Problem: 27. Remove Element
Approach: Two-pointer technique (Reader/Writer). Modifies the array in-place by overwriting elements that match the target value, avoiding extra memory allocation.

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        writer = 0

        for reader in range(len(nums)):
            if nums[reader] != val:
                nums[writer] = nums[reader]
                writer += 1
                
        return writer
