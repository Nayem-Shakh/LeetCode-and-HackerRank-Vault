"""
Problem: 374. Guess Number Higher or Lower
Approach: Binary Search. The algorithm queries a pre-defined API to navigate the search space. It calculates the midpoint using `low + (high - low) // 2` to strictly prevent integer overflow (a crucial safeguard in strictly-typed languages), adjusting the search boundaries based on the API's feedback until the exact number is found.

Time Complexity: O(\log N) where N is the maximum possible number.
Space Complexity: O(1) auxiliary space.
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            mid = low + (high - low) // 2
            result = guess(mid)
            
            if result == 0:
                return mid
            elif result == -1:
                high = mid - 1
            else: 
                low = mid + 1
                
        return -1