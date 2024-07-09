class FileHandler:
    @staticmethod
    def read_text_file(file_path):
        """
        Read the contents of a text file.

        Args:
            file_path (str): The path to the text file.

        Returns:
            str or None: The contents of the text file if it exists, otherwise None.
        """
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return None

    @staticmethod
    def write_text_file(file_path, text):
        """
        Writes text to a file specified by file_path.

        Parameters:
            file_path (str): The path to the file where the text will be written.
            text (str): The text to be written to the file.
        """
        with open(file_path, 'w') as file:
            file.write(text)