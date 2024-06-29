# Proyecto Trabajo Final - Ingeniería para Sistemas de Información - Nicolás Leidi

## Introducción

Creación de batería de testing de prolog automatizado y herramienta de verificación para problemas con fines académicos

## Requerimientos

-   Python 3.6 o superior
-   SWI-Prolog 8.2 o superior
-   La librería `pyswip` es necesaria
-   La librería `tkinter-tooltip` es necesaria

## Utilización

Los primeros pasos para utilizar la aplicación son:

1.  Presionar el botón **Cargar Base de Conocimiento**.
2.  Elegir el archivo de base de conocimiento de PROLOG.

### Testear un programa

Para testear un programa tiene que realizar:

1.  Presionar el botón de **Modo de Prueba**.
2.  Elegir el archivo de casos de prueba.
3.  Se cargarán todos los casos de prueba en la ventana.
4.  Presionar el botón de **Correr**.

Los resultados de las pruebas se mostrarán en la ventana, siendo rojo casos de prueba no pasados y en verde los que se pasaron correctamente.

### Creación de batería de tests

Para crear una batería de tests tiene que realizar:

1.  Presionar el botón de **Modo de Creación**.
2.  En el cuadro de arriba podrá escribir las consultas a probar, el cuadro de abajo mostrará las consultas ya cargadas.

    -   Puede presionar en los checkbox de abajo para configurar el tipo de comparación al momento de correr los casos de prueba:
        -   **Sin Orden**: compara los conjuntos de resultados sin importar el orden.
        -   **Primer Resultado**: solo compara la primera unificación de ambos resultados.
    -   Si se seleccionan ambos, se cumplirá si la primera unificación está contenida dentro de la resolución del programa a testear.
    -   Si no se selecciona ninguna, se cumplirá sí y solo sí la unificación del programa elegido y el de testear son iguales.
    -   En caso de ser un test negativo (que debe de daro falso), estas opciones no afectan al resultado, solo va a ser verdadero sí y solo sí el programa a testear falla.

3.  Cargar las consultas a la batería con los botones.

    -   **Agregar**: coloca las consultas en la batería de tests.
    -   **Guardar**: guarda la batería de tests en un archivo.
    -   **Deshacer**: elimina la última consulta de la batería de tests.
    -   **Limpiar**: elimina todas las consultas de la batería de tests.

4.  Cuando se termine de agregar consultas, presionar en **Guardar**.
5.  Elegir el archivo en donde se guardarán las consultas.
