from typing import List

"""
Problem: 150. Evaluate Reverse Polish Notation
Approach: Stack-based evaluation. The algorithm iterates through the tokens, pushing numbers onto a stack. When an operator is encountered, it pops the top two numbers, applies the operation, and pushes the result back. Division strictly uses `int()` conversion rather than floor division (`//`) to correctly handle truncation toward zero for negative numbers.

Time Complexity: O(N) where N is the number of tokens, as each token is processed exactly once.
Space Complexity: O(N) auxiliary space for the stack in the worst-case scenario.
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        number_stack = []

        for current_token in tokens:
            if current_token in "+-*/":
                right_operand = number_stack.pop()
                left_operand = number_stack.pop()

                if current_token == "+":
                    number_stack.append(left_operand + right_operand)
                elif current_token == "-":
                    number_stack.append(left_operand - right_operand)
                elif current_token == "*":
                    number_stack.append(left_operand * right_operand)
                elif current_token == "/":
                    number_stack.append(int(left_operand / right_operand))
            else:
                number_stack.append(int(current_token))
                
        return number_stack[0]