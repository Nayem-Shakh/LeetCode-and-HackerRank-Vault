"""
Problem: 167. Two Sum II - Input Array Is Sorted
Approach: Two-pointer technique. Because the input is already sorted, we place pointers at the opposite ends. If the sum is too small, the left pointer moves up; if it is too large, the right pointer moves down.

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1