"""
Problem: 345. Reverse Vowels of a String
Approach: Two-pointer technique combined with a Hash Set for O(1) vowel lookups. Converts the string to a list for in-place swapping as the left and right pointers converge on vowels.

Time Complexity: O(N) where N is the length of the string.
Space Complexity: O(N) to store the string as a mutable list.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = set("aeiouAEIOU")
        s_list = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and s_list[left] not in vowel:
                left += 1
            while left < right and s_list[right] not in vowel:
                right -= 1
                
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
                
        return "".join(s_list)