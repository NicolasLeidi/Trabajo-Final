import re

class PredicateInstance:

    # Ignorar, era parte de lo necesario para el modelo
    def __init__(self, predicate, instance):
        self.predicate = predicate
        self.instance = instance

    def dissect(self, instance):
        self.name, parameters = instance.split("(")
        parameters = parameters.strip(")").strip()
        
        # Patrón para separar los parámetros aunque tengan listas
        param_pattern = r'\[[^\[\]]*\]|[^,]+'
    
        parameters = re.findall(param_pattern, instance)
        
        self.inputs = []
        self.outputs = []
        self.inputs_or_outputs = []
        
        components = parameters.split(",")
        
        for component in components:
            
            # Remuevo espacios de más
            component = component.strip()
            
            # Lo agrego a la lista de parámetros ordenados
            self.parameters_ordered.append(component)

    def __str__(self):
        return self.instance
    
if __name__ == "__main__":
    # param_pattern = r'\[[^\[\]]*\]|[^,]+'
    param_pattern = r""
    instance = 'instance([1, [2], 3], 1 , 2 , 3, "example")'
    name, parameters = instance.split("(")
    parameters = parameters.strip(")").strip()
    
    result = re.findall(param_pattern, parameters)
    print(result)
    
    test = '"3"'
    print(test.isnumeric())