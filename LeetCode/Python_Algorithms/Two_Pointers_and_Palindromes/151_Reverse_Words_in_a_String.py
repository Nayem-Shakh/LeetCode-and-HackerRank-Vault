"""
Problem: 151. Reverse Words in a String
Approach: Utilizes Python's built-in string methods. The .split() method elegantly extracts the words while automatically stripping leading, trailing, and multiple spaces. The list is then reversed using slicing [::-1] and rejoined into a cleanly formatted string.

Time Complexity: O(N) where N is the length of the string.
Space Complexity: O(N) to store the array of split words.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        words_in_order = s.split()
        words_reversed = words_in_order[::-1]
        
        return " ".join(words_reversed)