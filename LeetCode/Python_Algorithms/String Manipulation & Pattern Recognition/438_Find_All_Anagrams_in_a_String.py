from typing import List

"""
Problem: 438. Find All Anagrams in a String
Approach: Sliding Window with Frequency Maps. Maintains a target frequency dictionary for string `p` and dynamically updates a sliding window dictionary across string `s`. By adding the new incoming character and removing the outgoing character, the algorithm efficiently compares the states of the window in constant time.

Time Complexity: O(N) where N is the length of string s. The dictionary comparison takes O(1) time because the maximum number of unique keys is bounded at 26 (lowercase English letters).
Space Complexity: O(1) auxiliary space, as the frequency dictionaries will store at most 26 key-value pairs.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        count_p = {}
        window_count = {}

        for chr in p:
            count_p[chr] = count_p.get(chr, 0) + 1

        result = []

        for i in range(len(s)):
            new_chr = s[i]
            window_count[new_chr] = window_count.get(new_chr, 0) + 1

            if i >= len(p):
                old_chr = s[i - len(p)]
                if window_count[old_chr] == 1:
                    del window_count[old_chr]
                else: 
                    window_count[old_chr] -= 1
            
            if window_count == count_p:
                result.append(i - len(p) + 1)
                
        return result