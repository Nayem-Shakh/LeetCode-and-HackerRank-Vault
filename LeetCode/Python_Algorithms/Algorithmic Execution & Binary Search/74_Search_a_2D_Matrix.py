from typing import List

"""
Problem: 74. Search a 2D Matrix
Approach: Abstracted 1D Binary Search. Since the matrix is strictly sorted both across rows and top-to-bottom, it can be treated logically as a single flattened 1D array. The algorithm runs a standard binary search, using integer division (//) and modulo (%) to dynamically map the 1D midpoint index back to its 2D row and column coordinates.

Time Complexity: O(\log(M \times N)) where M is the number of rows and N is the number of columns.
Space Complexity: O(1) auxiliary space.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = mid // cols, mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False