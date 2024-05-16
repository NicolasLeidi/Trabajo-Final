from utils.Stringify import Stringify

class PredicateDefinition:
    def __init__(self, predicate):
        self.dissect(predicate)
        self.instances = []
    
    def dissect(self, predicate):
        self.name, parameters = predicate.split("(")
        
        # Remuevo el punto y el paréntesis del final
        parameters = parameters.strip(")").strip()
        
        self.input_parameters = []
        self.output_parameters = []
        self.input_or_output_parameters = []
        self.parameters_ordered = []
        
        components = parameters.split(",")
        
        for component in components:
            
            # Remuevo espacios de más
            component = component.strip()
            
            # Lo agrego a la lista de parámetros ordenados
            self.parameters_ordered.append(component)
            
            if component.startswith("+"):
                self.input_parameters.append(component[1:])
            elif component.startswith("-"):
                self.output_parameters.append(component[1:])
            elif component.startswith("?"):
                self.input_or_output_parameters.append(component[1:])
    
    # Rearmo el predicado, colocando las listas recibidas respetando el orden inicial
    def rearm(self, inputs, outputs, inputs_or_outputs):
        predicate = self.name + "("	
        i, j, k = 0, 0, 0
        
        # Los coloco en el orden que fueron definidos
        for parameter in self.parameters_ordered:
            if parameter.startswith("+"):
                predicate += Stringify.stringify(inputs[i])
                i += 1
            elif parameter.startswith("-"):
                predicate += Stringify.stringify(outputs[j])
                j += 1
            elif parameter.startswith("?"):
                predicate += Stringify.stringify(inputs_or_outputs[k])
                k += 1
            predicate += ","
        predicate = predicate.strip(",")
        predicate += ")"
        return predicate        
    
    def __str__(self):
        predicate = self.name + "("
        for parameter in self.parameters_ordered:
            predicate += parameter + ","
        predicate = predicate.strip(",")
        predicate += ")"
        return predicate
    