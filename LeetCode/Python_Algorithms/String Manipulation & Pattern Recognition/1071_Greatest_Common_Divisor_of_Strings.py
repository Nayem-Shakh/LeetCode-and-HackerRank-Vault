import math

"""
Problem: 1071. Greatest Common Divisor of Strings
Approach: Mathematical String Concatenation. If two strings are constructed from the same repeating substring, concatenating them in either order must produce the identical string. Once validated, the length of the greatest common divisor string is exactly the mathematical GCD of their lengths.

Time Complexity: O(N + M) where N and M are the lengths of the two strings (due to string concatenation and comparison).
Space Complexity: O(N + M) auxiliary space required to create the concatenated strings for comparison.
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        gcd_length = math.gcd(len(str1), len(str2))

        return str1[:gcd_length]