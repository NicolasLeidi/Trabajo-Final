class PrologPredicate:
    def __init__(self, predicate):
        self.dissect(predicate)
    
    def dissect(self, predicate):
        self.name, parameters = predicate.split("(")
        
        # Remuevo el punto y el paréntesis del final
        parameters = parameters.strip(")").strip()
        
        self.input_parameters = []
        self.output_parameters = []
        self.input_or_output_parameters = []
        
        components = parameters.split(",")
        
        for component in components:
            
            # Remuevo espacios de más
            component = component.strip()
            
            if component.startswith("+"):
                self.input_parameters.append(component[1:])
            elif component.startswith("-"):
                self.output_parameters.append(component[1:])
            elif component.startswith("?"):
                self.input_or_output_parameters.append(component[1:])
    