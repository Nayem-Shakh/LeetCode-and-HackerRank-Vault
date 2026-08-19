"""
Problem: 278. First Bad Version
Approach: Binary Search. Instead of searching for an exact match, the algorithm searches for the first instance of a true condition (a boundary). When a bad version is found, it records the version and narrows the search space to the left to see if an earlier bad version exists. If the version is good, it narrows the search space to the right.

Time Complexity: O(\log N) where N is the number of versions.
Space Complexity: O(1) auxiliary space.
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left_pointer = 1
        right_pointer = n
        earliest_bad_version = -1

        while left_pointer <= right_pointer:
            middle_version = (left_pointer + right_pointer) // 2

            if isBadVersion(middle_version):
                earliest_bad_version = middle_version
                right_pointer = middle_version - 1
            else: 
                left_pointer = middle_version + 1
                
        return earliest_bad_version