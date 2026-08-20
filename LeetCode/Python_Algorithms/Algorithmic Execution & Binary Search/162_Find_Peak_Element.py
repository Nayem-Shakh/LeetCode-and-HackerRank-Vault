from typing import List

"""
Problem: 162. Find Peak Element
Approach: Binary Search on Unsorted Array. By treating the array boundaries as negative infinity, the algorithm simply evaluates the local gradient (slope). It compares the midpoint to its immediate right neighbor. If the midpoint is greater, the slope is falling, meaning a peak must exist to the left (including the midpoint). Otherwise, the slope is rising, and a peak must exist strictly to the right. 

Time Complexity: O(log N) where N is the length of the array.
Space Complexity: O(1) auxiliary space.
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            else: 
                left = mid + 1
                
        return left