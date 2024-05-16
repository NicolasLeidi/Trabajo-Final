import re


class Unstringify:
    
    @staticmethod
    def unstringify(data):
        unstringified = []
        pattern = r'\[[^\[\]]*\]|[^,]+'
        components = re.findall(pattern, data.strip())
        for component in components:
            component = component.strip()
            unstringified.append(Unstringify.parse_component(component))
        return unstringified
    
    @staticmethod
    def parse_component(component):
        if component.isnumeric():
            return int(component)
        elif component.startswith('[') and component.endswith(']'):
            # Handle nested lists by recursively unstringifying the content inside the square brackets
            return Unstringify.unstringify(component[1:-1])
        else:
            return component  # Return as is
    

if __name__ == "__main__":
    tests = Unstringify.unstringify('[[1, 2, 3], "3", [4, 5] , 5]')
    for test in tests:
        print(test)