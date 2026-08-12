"""
Problem: 647. Palindromic Substrings
Approach: Expand Around Center using Two Pointers. Iterates through the string and expands outward from every possible center (both single characters and pairs) to count all valid palindromes.

Time Complexity: O(N^2) where N is the length of the string.
Space Complexity: O(1)
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        total_count = 0

        for i in range(len(s)):
            
            # Odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                total_count += 1
                l -= 1
                r += 1

            # Even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                total_count += 1
                l -= 1
                r += 1

        return total_count
