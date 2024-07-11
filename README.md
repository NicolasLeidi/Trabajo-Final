# SwipTesting - Proyecto Trabajo Final - Ingeniería para Sistemas de Información - Nicolás Leidi

## Introducción

Creación de batería de testing de prolog automatizado y herramienta de verificación para problemas con fines académicos

## Requerimientos

Para los ejecutables, se necesita

-   SWI-Prolog 8.2 o superior
-   Distribución x64 de Windows

Para compilar y ejecutar los archivos main, se necesita:

-   Python 3.6 o superior
-   SWI-Prolog 8.2 o superior
-   La librería `pyswip` es necesaria
-   La librería `tkinter-tooltip` es necesaria
-   La librería `pyparsing` es necesaria

## Utilización de la GUI

Puede ejecutar tanto la versión de alumno (`student_main.exe`) como la de profesor (`teacher_main.exe`)

### Testear un programa

Los primeros pasos para utilizar la aplicación para probar un programa son:

1.  Presionar el botón **Cargar Base de Conocimiento**.
2.  Elegir el archivo de base de conocimiento de PROLOG.
3.  Presionar el botón de **Probar**.
4.  Elegir el/los archivo/s de casos de prueba.
5.  Se cargarán todos los casos de prueba en la ventana.

    -   **Agregar Ejemplos** permite agregar más archivos de casos de prueba.
    -   **Limpiar** permite eliminar todos los casos de prueba que se hayan cargado.
    -   **Remover** permite eliminar el caso de prueba seleccionado con un click del mouse previamente.

6.  Presionar el botón de **Correr**.

    -   En la parte inferior derecha se puede ver la cantidad de tests exitosos.
    -   En verde se pueden ver los tests exitosos
    -   En rojo se pueden ver los tests que fallaron, junto una explicación y la comparación entre resultado esperado y el que el que recibió
    -   **Volver** Se vuelve a la ventana anterior a ver los resultados.

### Creación de batería de tests

Para crear una batería de tests tiene que realizar:

1.  Presionar el botón de **Crear Tests**.
2.  En el cuadro de arriba podrá escribir las consultas a probar, el cuadro del medio el resultado esperado y en el cuadro de abajo mostrará las consultas ya cargadas.

    -   Puede presionar en los checkbox de abajo para configurar el tipo de comparación al momento de correr los casos de prueba:
        -   **Sin Orden**: compara los conjuntos de resultados sin importar el orden.
        -   **Primer Resultado**: solo compara la primera unificación de ambos resultados.
    -   Si se seleccionan ambos, se cumplirá si la primera unificación está contenida dentro de la resolución del programa a testear.
    -   Si no se selecciona ninguna, se cumplirá sí y solo sí la unificación del programa elegido y el de testear son iguales.
    -   En caso de ser un test negativo (que debe de daro falso), estas opciones no afectan al resultado, solo va a ser verdadero sí y solo sí el programa a testear falla.

3.  Escriba en el cuadro superior (`Crear Query de Caso de Prueba`) la query a probar. Tenga en cuenta que solo se puede ingresar una query a la vez.
4.  Escriba en el cuadro del medio (`Resultado Esperado del Caso de Prueba`) el resultado que debería dar esa query. Tenga en cuenta la sintaxis:

    -   Si el resultado es verdadero sin ninguna unificación o falso, colocar True o False respectivamente.
    -   Si el resultado es verdadero con unificaciones, colocar las variables como:
        -   Variable : Valor
        -   Múltiples variables en la misma respuesta deben estar separadas con ampersand (&)
        -   Múltiples conjuntos de unificaciones válidos separados por enter

5.  Cargar las consultas a la batería con los botones.

    -   **Agregar**: coloca las consultas en la batería de tests.
    -   **Guardar**: guarda la batería de tests en un archivo.
    -   **Deshacer**: elimina la última consulta de la batería de tests.
    -   **Limpiar**: elimina todas las consultas de la batería de tests.

6.  Cuando se termine de agregar consultas, presionar en **Guardar**.
7.  Elegir el archivo en donde se guardarán las consultas.

### Creación de batería de tests asistido

Esta funcionalidad está solo disponible para la versión de profesores (`teacher_main.exe`), ya que requiere una correcta resolución al problema para crear la batería de tests.

1.  Presionar el botón **Cargar Base de Conocimiento**.
2.  Elegir el archivo de base de conocimiento de PROLOG.
3.  Presionar el botón de **Crear Tests Asistido**.
4.  En el cuadro de arriba podrá escribir las consultas a probar, el cuadro de abajo mostrará las consultas ya cargadas.

    -   Puede presionar en los checkbox de abajo para configurar el tipo de comparación al momento de correr los casos de prueba:
        -   **Sin Orden**: compara los conjuntos de resultados sin importar el orden.
        -   **Primer Resultado**: solo compara la primera unificación de ambos resultados.
    -   Si se seleccionan ambos, se cumplirá si la primera unificación está contenida dentro de la resolución del programa a testear.
    -   Si no se selecciona ninguna, se cumplirá sí y solo sí la unificación del programa elegido y el de testear son iguales.
    -   En caso de ser un test negativo (que debe de daro falso), estas opciones no afectan al resultado, solo va a ser verdadero sí y solo sí el programa a testear falla.

5.  Cargar las consultas a la batería con los botones.

    -   **Agregar**: coloca las consultas en la batería de tests.
    -   **Guardar**: guarda la batería de tests en un archivo.
    -   **Deshacer**: elimina la última consulta de la batería de tests.
    -   **Limpiar**: elimina todas las consultas de la batería de tests.

6.  Cuando se termine de agregar consultas, presionar en **Guardar**.
7.  Elegir el archivo en donde se guardarán las consultas.

## Utilización de la versión de consola

Para probar por consola se tiene que llamar al ejecutable de consola (`console_main.exe`) con los siguientes argumentos:

    -   Primer argumento: el archivo .pl de base de conocimiento.
    -   Segundo argumento en adelante: archivos o carpetas de batería de tests
        -   Los archivos tienen que tener terminación .json
        -   De cada carpeta ingresada se buscará archivos .json en esa carpeta, sin buscar en dentro de carpetas dentro.
