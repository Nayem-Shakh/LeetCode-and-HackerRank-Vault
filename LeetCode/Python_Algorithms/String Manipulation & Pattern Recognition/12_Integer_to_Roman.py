"""
Problem: 12. Integer to Roman
Approach: Greedy Algorithm. Utilizes a predefined lookup table containing Roman numeral symbols and their integer values in descending order (including special subtraction cases like 'IV' and 'CM'). Iterates through the table, greedily appending the largest possible symbol to the result string and subtracting its value from the number until the number reaches zero.

Time Complexity: O(1) because the maximum input is 3999, meaning the while loop runs a strictly bounded, constant maximum number of times.
Space Complexity: O(1) as the lookup table is a fixed size and the maximum length of the output string is also bounded.
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_table = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), 
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), 
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        result = ""

        for value, symbol in roman_table:
            while num >= value:
                result += symbol
                num -= value

        return result