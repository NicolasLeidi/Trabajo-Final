class Stringify:

    @staticmethod
    def stringify(data):
        stringified = ""
        if isinstance(data, int):
            stringified = str(data)
        elif isinstance(data, str):
            stringified = data
        elif isinstance(data, list):
            stringified_elements = [Stringify.stringify(element) for element in data]
            stringified = "[" + ", ".join(stringified_elements) + "]"
        else:
            raise ValueError("Unsupported data type: " + str(type(data)))
        return stringified