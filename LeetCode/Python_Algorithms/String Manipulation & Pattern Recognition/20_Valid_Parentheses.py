"""
Problem: 20. Valid Parentheses
Approach: Uses a Stack to keep track of opening brackets and a Hash Map to match closing brackets. Iterates through the string, pushing opening brackets onto the stack. When a closing bracket is found, it pops the top of the stack and verifies it is the correct matching bracket.

Time Complexity: O(N) where N is the length of the string.
Space Complexity: O(N) in the worst-case scenario where the string contains only opening brackets.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch not in match:
                stack.append(ch)
            else:
                if not stack:
                    return False

                top = stack.pop()

                if top != match[ch]:
                    return False
                    
        return len(stack) == 0