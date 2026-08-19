from typing import List

"""
Problem: 35. Search Insert Position
Approach: Binary Search. The algorithm systematically halves the search space to find the target. If the target is not found, the loop terminates when the pointers cross. At this exact moment, the left pointer will naturally sit at the correct insertion index to maintain the array's sorted order.

Time Complexity: O(\\log N) where N is the number of elements in the array.
Space Complexity: O(1) auxiliary space.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            middle_index = (left_pointer + right_pointer) // 2

            if nums[middle_index] == target:
                return middle_index
            elif nums[middle_index] < target:
                left_pointer = middle_index + 1
            else:
                right_pointer = middle_index - 1

        return left_pointer