from typing import List

"""
Problem: 704. Binary Search
Approach: Iterative Binary Search. The algorithm maintains two pointers (left and right) to define the active search space. By calculating the middle index and comparing it to the target, it effectively halves the remaining search space on each iteration until the target is found or the pointers cross.

Time Complexity: O(\log N) where N is the number of elements in the array, as the search space is divided by two at each step.
Space Complexity: O(1) auxiliary space.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
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

        return -1