"""
Problem: 5. Longest Palindromic Substring
Approach: Expand Around Center using Two Pointers. Iterates through the string, expanding outward from every possible center (odd and even lengths) to dynamically track and update the longest valid palindrome found.

Time Complexity: O(N^2) where N is the length of the string.
Space Complexity: O(1) auxiliary space (excluding the output string).
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        for i in range(len(s)):
            
            # Odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(result):
                    result = s[l:r+1]
                l -= 1
                r += 1

            # Even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(result):
                    result = s[l:r+1]
                l -= 1
                r += 1
                
        return result