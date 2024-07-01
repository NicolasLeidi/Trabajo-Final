import ast

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
    
    @staticmethod
    def unstringify(data):
        if data.isnumeric():
            return int(data)
        elif data[0] == '[' and data[-1] == ']':
            transformed_list = ast.literal_eval(data)
        
            # Iterate through the list and process elements if necessary
            for i, element in enumerate(transformed_list):
                if isinstance(element, str) and element.isdigit():
                    transformed_list[i] = int(element)
        
            return transformed_list
        else:
            return data