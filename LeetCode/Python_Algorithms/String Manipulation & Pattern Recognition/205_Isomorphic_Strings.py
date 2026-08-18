"""
Problem: 205. Isomorphic Strings
Approach: Uses two Hash Maps to track character mappings from s to t and from t to s. Iterates through both strings simultaneously using zip(), ensuring a strict one-to-one bijection between characters.

Time Complexity: O(N) where N is the length of the strings.
Space Complexity: O(1) auxiliary space, as the maximum number of unique ASCII characters is fixed (at most 256).
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for cs, ct in zip(s, t):
            if cs in s_to_t:
                if s_to_t[cs] != ct:
                    return False
            else:
                s_to_t[cs] = ct
                
            if ct in t_to_s:
                if t_to_s[ct] != cs:
                    return False
            else:
                t_to_s[ct] = cs
                
        return True