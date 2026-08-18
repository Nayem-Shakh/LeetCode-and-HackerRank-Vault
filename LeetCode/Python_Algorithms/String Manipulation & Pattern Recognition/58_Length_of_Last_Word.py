"""
Problem: 58. Length of Last Word
Approach: Reverse iteration. Iterates through the string backwards to first skip any trailing spaces, then counts the characters of the last word until the next space or the beginning of the string is reached. This manual traversal avoids the O(N) space penalty of using the built-in split() method.

Time Complexity: O(N) in the worst case, but practically O(L) where L is the length of the trailing spaces plus the last word.
Space Complexity: O(1)
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1
        
        if i < 0:
            return 0
        
        count = 0
        
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1
        
        return count