from typing import List

"""
Problem: 33. Search in Rotated Sorted Array
Approach: Modified Binary Search. The algorithm relies on the property that in a rotated sorted array, at least one half of the array (either left to mid, or mid to right) must be strictly sorted. It first determines which half is sorted, then checks if the target falls within the bounds of that sorted half to decide which way to move the pointers.

Time Complexity: O(\\log N) where N is the length of the array.
Space Complexity: O(1) auxiliary space.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1