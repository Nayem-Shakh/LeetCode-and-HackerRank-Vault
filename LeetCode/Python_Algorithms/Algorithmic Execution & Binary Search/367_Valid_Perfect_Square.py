"""
Problem: 367. Valid Perfect Square
Approach: Binary Search. Instead of using built-in square root functions, this algorithm systematically searches for the square root. It optimizes the initial search space by setting the upper bound to `num // 2`, since the square root of any number greater than or equal to 4 will never exceed half of the number itself.

Time Complexity: O(log N) where N is the given number.
Space Complexity: O(1) auxiliary space.
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left, right = 2, num // 2

        while left <= right:
            mid = left + (right - left) // 2
            squared = mid * mid

            if squared == num:
                return True
            elif squared < num:
                left = mid + 1
            else:
                right = mid - 1
                
        return False