from typing import List

"""
Problem: 153. Find Minimum in Rotated Sorted Array
Approach: Modified Binary Search. Since the sorted array is rotated, the algorithm compares the midpoint element to the rightmost element. If the midpoint is strictly greater than the rightmost element, the minimum (the pivot point) must exist in the right half. Otherwise, the midpoint itself could be the minimum, so the right pointer is pulled exactly to mid. The loop terminates when left and right converge on the absolute minimum.

Time Complexity: O(log N) where N is the length of the array.
Space Complexity: O(1) auxiliary space.
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else: 
                right = mid

        return nums[left]