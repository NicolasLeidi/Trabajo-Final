import ast
import json

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
        """
        Converts a string representation of a value into its corresponding Python object, between int, list or a string.

        Args:
            data (str): The string representation of the value.

        Returns:
            Union[int, list, str]: The converted value. If the string is a numeric value, it is converted to an integer.
            If the string is a list in the format '[element1, element2, ...]', the elements are converted to their
            corresponding Python objects. If the string is not a numeric value or a list, it is returned as is.
        """
        data = data.strip()
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

    @staticmethod
    def replace_byte_strings(dict):
        """
        Replaces byte strings in the values of a dictionary with their corresponding string representation.

        Args:
            dict (dictionary): A dictionary, where some values may be byte strings.

        Returns:
            dictionary: A new dictionary with the same items as the input dictionary, but with byte strings replaced by their string representation.
        """
        new_dict = {}
        for key, value in dict.items():
            if isinstance(value, bytes):
                # Decode bytes to string, replace single quotes with double quotes
                decoded_item = value.decode('utf-8')
                replaced_item = '"' + decoded_item + '"'
                new_dict[key] = replaced_item
            else:
                new_dict[key] = value
        return new_dict