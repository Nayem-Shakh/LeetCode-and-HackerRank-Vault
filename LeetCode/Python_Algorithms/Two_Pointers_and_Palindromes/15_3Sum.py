"""
Problem: 15. 3Sum
Approach: Sorts the array first to enable the two-pointer technique. Iterates through the array, treating each element as a fixed target, and uses left and right pointers to find the complement. Includes specific conditions to skip adjacent duplicates and avoid redundant triplets.

Time Complexity: O(N^2) where N is the length of the array. Sorting takes O(N log N) and the nested loops take O(N^2).
Space Complexity: O(1) auxiliary space (or O(N) depending on the language's sorting algorithm implementation), excluding the output array.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1
                    
        return res