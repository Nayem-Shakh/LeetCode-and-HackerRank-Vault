"""
Problem: 290. Word Pattern
Approach: Uses two Hash Maps to create a strict bijection (one-to-one mapping) between characters in the pattern and words in the string. An initial length check ensures the pattern and word count match before iterating.

Time Complexity: O(N) where N is the length of the string s, primarily for the .split() operation.
Space Complexity: O(N) auxiliary space to store the array of words created by .split() and the Hash Maps.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False
            
        p_to_w = {}
        w_to_p = {}

        for cp, cw in zip(pattern, words):
            if cp in p_to_w:
                if p_to_w[cp] != cw:
                    return False
            else:
                p_to_w[cp] = cw
            
            if cw in w_to_p:
                if w_to_p[cw] != cp:
                    return False
            else:
                w_to_p[cw] = cp
                
        return True