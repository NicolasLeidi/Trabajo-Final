import json
import sys
import os
from model.prolog.PrologInterface import PrologInterface
from utils.FeedbackEnum import FeedbackEnum
from utils.FileHandler import FileHandler

def process_battery_test_folder(path):
    for files in os.listdir(path):
        # Agarro solo los archivos .json, ya que las baterías de tests se guardan en archivos .json
        if files.endswith(".json"):
            # Como el file handler requiere un path al archivo, uno el path al directorio acon el nombre del archivo
            process_battery_test(os.path.join(path, files))
    
def process_battery_test(path):
    examples = json.loads(FileHandler.read_text_file(path))
    try:
        for example in examples:
            prolog_interface.add_example_to_base(example)
    except Exception:
        print(f"Error al cargar el ejemplo: {examples}")
        sys.exit()
    

if len(sys.argv) < 3:
    print("Faltan argumentos. Por favor, introduzca base de conocimiento y al menos una batería de test.")
    sys.exit()

knowledge_base_path = sys.argv[1]
battery_test_paths = sys.argv[2:]

prolog_interface = PrologInterface()

# Reemplazar \ por / por requerimiento de pyswip
knowledge_base_path = knowledge_base_path.replace("\\", "/")

if not os.path.exists(knowledge_base_path):
    sys.exit(f"Base de conocimiento no encontrada en: {knowledge_base_path}")

# Cargar la base de conocimiento y luego consultarla
prolog_interface.set_knowledge_base(knowledge_base_path)
prolog_interface.consult_knowledge_base()

for path in battery_test_paths:
    if not os.path.exists(path):
        print(f"Archivo o carpeta de batería de test no encontrada: {path}")
        continue
    
    # Si es un archivo, cargo el archivo, si es una carpeta, proceso los archivos dentro de esa carpeta
    if os.path.isfile(path):
        process_battery_test(path)
    elif os.path.isdir(path):
        process_battery_test_folder(path)


try:
    results = prolog_interface.test_examples()
    
    total_tests = len(results)
    completed_tests = 0
    
    for [query, result_code, results, expected_results, explanation] in results:
        if result_code == FeedbackEnum.SUCCESS:
            completed_tests += 1
        else:
            print(f"Test {query} - {result_code.name} - {explanation}\nSe esperaba:\n{expected_results}\nSe obtuvo:\n{results}\n")
    print(f"Test exitosos: {completed_tests}/{total_tests}")
except Exception:
    print("Error al correr las pruebas. La sintaxis de los casos de prueba es incorrecta.")
    sys.exit()