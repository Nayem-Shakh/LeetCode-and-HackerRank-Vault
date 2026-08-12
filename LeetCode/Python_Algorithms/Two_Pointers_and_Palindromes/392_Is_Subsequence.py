"""
Problem: 392. Is Subsequence
Approach: Two-pointer technique across two strings. Uses one pointer to track the target subsequence and another to traverse the main string, advancing the target pointer only when a character match is found.

Time Complexity: O(N) where N is the length of string t.
Space Complexity: O(1)
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        len_s, len_t = len(s), len(t)

        while i < len_s and j < len_t:
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len_s