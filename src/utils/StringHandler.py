from pyparsing import Word, alphas, alphanums, nums, Group, Forward, oneOf, ZeroOrMore, Suppress, Optional

class StringHandler:
    
    @staticmethod
    def check_brackets_are_balanced(string: str) -> bool:
        """
        Check if the brackets in the given string are balanced.

        Args:
            string (str): The string to check for balanced brackets.

        Returns:
            bool: True if the brackets are balanced, False otherwise.
        """
        stack = []
        brackets = {'(': ')', '[': ']'}
        
        for char in string:
            if char in brackets:
                stack.append(char)
            elif char in brackets.values():
                if not stack or brackets[stack.pop()] != char:
                    return False

        return not stack