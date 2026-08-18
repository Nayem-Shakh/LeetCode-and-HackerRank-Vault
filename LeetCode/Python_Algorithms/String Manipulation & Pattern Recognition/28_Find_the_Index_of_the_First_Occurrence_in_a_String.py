"""
Problem: 28. Find the Index of the First Occurrence in a String
Approach: Brute-force substring search using a sliding window. Iterates through the haystack and attempts to match the needle character by character. The outer loop is optimized to stop at n - m + 1 to avoid unnecessary out-of-bounds checks.

Time Complexity: O(N * M) where N is the length of the haystack and M is the length of the needle.
Space Complexity: O(1) auxiliary space.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
            
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            matched = True
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    matched = False
                    break

            if matched:
                return i
                
        return -1