from typing import List

"""
Problem: 875. Koko Eating Bananas
Approach: Binary Search on Answer Space. Instead of searching an array, the algorithm searches the possible range of eating speeds (from 1 to the maximum pile size). It uses a nested helper function with optimized integer ceiling division `(pile + k - 1) // k` to calculate the total hours required for a given speed. The binary search systematically narrows the window to find the absolute minimum valid speed.

Time Complexity: O(N \\log M) where N is the number of piles and M is the maximum number of bananas in a single pile.
Space Complexity: O(1) auxiliary space.
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEatAll(k: int, h: int) -> bool:
            total_hours = 0
            for pile in piles:
                total_hours += (pile + k - 1) // k
            return total_hours <= h

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            
            if canEatAll(mid, h):
                right = mid
            else: 
                left = mid + 1
                
        return left