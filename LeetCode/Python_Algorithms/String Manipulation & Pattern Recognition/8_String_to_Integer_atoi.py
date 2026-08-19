"""
Problem: 8. String to Integer (atoi)
Approach: Linear string traversal. The algorithm sequentially processes the string by first skipping leading whitespaces, then determining the sign, and finally building the integer digit by digit. It handles out-of-bounds characters by terminating early and securely clamps the final result within the 32-bit signed integer range to prevent overflow.

Time Complexity: O(N) where N is the length of the string, as each character is visited at most once.
Space Complexity: O(1) auxiliary space, using only a few variables for state tracking.
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2147483648
        INT_MAX = 2147483647

        position = 0
        length = len(s)

        while position < length and s[position] == ' ':
            position += 1

        sign = 1

        if position < length and s[position] == '-':
            sign = -1
            position += 1
        elif position < length and s[position] == '+':
            position += 1

        number = 0

        while position < length and s[position].isdigit():
            number = number * 10 + int(s[position])
            position += 1

        number *= sign

        if number < INT_MIN:
            return INT_MIN
        if number > INT_MAX:
            return INT_MAX

        return number