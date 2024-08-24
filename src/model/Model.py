import json
from model.exception.PrologSyntaxException import PrologSyntaxException
from model.prolog.PrologInterface import PrologInterface
from utils.FileHandler import FileHandler

class Model():
    def __init__(self):
        self.prolog_interface = PrologInterface()
    
    def bind_presenter(self, presenter):
        """
        Bind the given presenter to the current instance.

        Parameters:
            presenter (object): The presenter object to be bound.
        """
        self.presenter = presenter
    
    def load_knowledge_base(self, knowledge_base_path):
        """
        Load the knowledge base from the given path.

        Parameters:
            knowledge_base_path (str): The path to the knowledge base file.

        Returns:
            tuple: A tuple containing a boolean value indicating success and the loaded text if successful, otherwise a boolean value and an error message.
        """
        text = FileHandler.read_text_file(knowledge_base_path)
        if text is not None:
            self.prolog_interface.set_knowledge_base(knowledge_base_path)
            self.prolog_interface.consult_knowledge_base()
            return(True, text)
        else:
            return(False, "Error")
    
    def add_examples(self, examples, ordered, first_only):
        """
        Adds examples to the model based on the given examples list, considering the order and first-only flags.

        Parameters:
            examples (str): A string containing examples separated by lines.
            ordered (bool): Flag indicating if the order of the results should not be preserved.
            first_only (bool): Flag indicating if only the first example should matter.

        Returns:
            tuple: A tuple containing a boolean value indicating success and a message about the operation outcome.
        """
        examples_list = examples.splitlines()
        try:
            for example in examples_list:
                self.prolog_interface.create_example(example, ordered, first_only)
            return (True, "Ejemplos agregados correctamente.")
        except PrologSyntaxException:
            self.presenter.show_message("Error", "Error al correr los ejemplos. Verifique la sintaxis de los ejemplos.")
            return (False, "Error")
    
    def add_manual_example(self, example, expected_result, ordered, first_only):
        """
        Adds a manually entered example to the model, along with its expected result, order flag, and first-only flag.

        Parameters:
            example (str): The example to add.
            expected_result (str): The expected result for the example.
            ordered (bool): Flag indicating if the order of the results should not be preserved.
            first_only (bool): Flag indicating if only the first example should matter.
        """
        self.prolog_interface.add_example_to_base([example, expected_result, ordered, first_only])
            
    def submit_examples(self, file_path):        
        """
        Submits examples to a specified file path.

        Parameters:
            file_path (str): The path to the file where the examples will be submitted.
        """
        try:
            FileHandler.write_text_file(file_path, json.dumps(self.prolog_interface.get_examples()))    
        except TypeError:
            self.presenter.show_message("Error", "Error al cargar los ejemplos.")
    
    def get_loaded_examples(self):
        """
        Returns the loaded examples from the Prolog interface.

        Returns:
            examples(list): A list of lists containing example strings, their results, order flags, and first-only flags.
        """
        return self.prolog_interface.get_examples()
    
    def clean_examples(self):
        """
        Cleans the examples in the model and updates the loaded examples text box in the view.
        """
        self.prolog_interface.empty_examples_base()
        
    def load_examples(self, file_paths):
        """
        A function that loads examples from file paths, adds them to the Prolog interface base,
        and returns the examples. If an exception occurs, the examples base is emptied and an error message is shown.
        
        Parameters:
            file_paths (list): A list of file paths containing examples to load.
        
        Returns:
            list: A list of loaded examples from the Prolog interface.
        """
        try:
            for file_path in file_paths:
                examples = json.loads(FileHandler.read_text_file(file_path))
                for example in examples:
                    self.prolog_interface.add_example_to_base(example)
            return(self.prolog_interface.get_examples())
        except Exception:
            self.prolog_interface.empty_examples_base()
            self.presenter.show_message("Error", "Error al cargar los ejemplos.")
    
    def run_examples(self):
        """
        Runs the examples in the model and returns the results.

        Returns:
            list: A list of feedbacks. Each feedback is a tuple containing the query, ordered, first_only, result code, actual results, expected results, and explanation (if any).

        Raises:
            Exception: If an error occurs while running the examples.
        """
        try:
            return self.prolog_interface.test_examples()
        except Exception:
            self.presenter.show_message("Error", "Error al correr las pruebas. La sintaxis de los casos de prueba es incorrecta.")
    
    def clean_examples(self):
        """
        Cleans the examples in the model by emptying the examples base.
        """
        self.prolog_interface.empty_examples_base()
    
    def pop_examples(self):
        """
        Removes an example from the examples base.
        """
        self.prolog_interface.pop_example_from_base()
    
    def pop_test(self, index):
        """
        Removes an example from the examples base.

        Parameters:
            index (int): The index of the example to be removed.
        """
        self.prolog_interface.pop_example_from_base(index)