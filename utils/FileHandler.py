class FileHandler:
    @staticmethod
    def read_text_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return None

    @staticmethod
    def write_text_file(file_path, text):
        with open(file_path, 'w') as file:
            file.write(text)