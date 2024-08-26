# SwipTesting - Proyecto Trabajo Final - Ingeniería para Sistemas de Información - Nicolás Leidi

## Introducción

Creación de batería de testing de prolog automatizado y herramienta de verificación para problemas con fines académicos

## Definición de términos

Query = consulta a ser ejecutada por el intérprete de SWI-Prolog

## Requerimientos técnicos

Para los ejecutables, se necesita

-   SWI-Prolog 8.2 o superior
-   Distribución x64 de Windows

Para compilar y ejecutar los archivos main, se necesita:

-   Python 3.6 o superior
-   SWI-Prolog 8.2 o superior
-   La librería `pyswip` 0.2.11 o superior
-   La librería `tkinter-tooltip` 3.1.0 o superior
-   La librería `pyparsing` 3.1.2 o superior

## Primer paso

Antes de poder ejecutar cualquiera de los programas se requiere ejecutar el archivo `set_prolog_home_dir.bat` en una consola de windows (cmd) para poder colocar la variable de entorno SWI_HOME_DIR que requiere la aplicación para funcionar.

-   Abrir una instancia de Command Prompt
-   Ejecutar el archivo `set_prolog_home_dir.bat`
-   Cerrar la consola

Ahora podrá ejecutar los archivos ejecutables.

## Utilización de la GUI

Puede ejecutar tanto la versión de alumno (`student_main.exe`) como la de profesor (`teacher_main.exe`)

### Testear un programa

Los primeros pasos para utilizar la aplicación para testear un programa son:

1.  Presionar el botón **Cargar Base de Conocimiento**.

![image](https://github.com/user-attachments/assets/d8669330-aa1e-4119-b25f-39bcfb3dad85)

> [!IMPORTANT]
> Dado limitaciones actuales, para cargar una nueva base de conocimiento se requiere cerrar y abrir la aplicación

2.  Elegir el archivo de base de conocimiento de PROLOG.
3.  Presionar en `Abrir` u `Open`.

![image](https://github.com/user-attachments/assets/3bc1dec3-3f14-4f6a-b973-3f295ba6dc09)

4.  Presionar el botón de **Probar**.

![image](https://github.com/user-attachments/assets/5d178b3f-2e1d-423a-9937-8a019d22b662)

5.  Elegir el/los archivo/s de casos de prueba que deben ser en formato .json.
6.  Presionar en `Abrir` u `Open`.

![image](https://github.com/user-attachments/assets/01fc7e5a-d90f-4016-b6c3-c258ca205a00)

7.  Se cargarán todas las queries de los casos de prueba seleccionados en el panel ubicado en la parte derecha de la ventana.

    -   **Agregar Ejemplos** permite agregar más archivos correspondientes a casos de prueba. Se repiten los pasos desde el paso 5.
    -   **Limpiar** permite eliminar todas las queries que se hayan cargado.
    -   **Remover** permite eliminar una query previamente seleccionada con un click del mouse.

Test seleccionado para remover:

![image](https://github.com/user-attachments/assets/cf02f229-0e96-478d-9606-c398e6a2c07e)


8.  Presionar el botón de **Correr**.

![image](https://github.com/user-attachments/assets/4b29b541-0591-4b95-99b2-34d10a464710)

-   En la parte inferior derecha de la ventana se puede ver visualizar la cantidad de tests exitosos.
-   En verde se pueden ver los tests exitosos.
-   En rojo se pueden ver los tests que fallaron, junto a una explicación del motivo que provocó el no éxito de cada test fallido y la comparación entre el resultado esperado y el resultado obtenido al ejecutar los tests.
-   Al presionar **Volver** Se se vuelve a la ventana anterior donde se muestran solo las query de prueba.

Ejemplo sin errores en la base de conocimiento

![image](https://github.com/user-attachments/assets/30aa6eca-1039-4894-be15-79b80f14f5e2)

Ejemplo con errores en la base de concoimiento

![image](https://github.com/user-attachments/assets/6f4d6990-dc01-422f-822c-92cd16b29cf9)

### Creación de batería de tests - Modo manual

Para crear una batería de tests se deben seguir los siguientes pasos:

1.  Presionar el botón **Crear Tests**.

![image](https://github.com/user-attachments/assets/1062052f-9875-447b-a211-833596df2eac)

-   En el cuadro ubicado en el extremo superior de la ventana deberá escribir las consultas que corresponden a los casos de test, y en el cuadro del medio deberá indicar el resultado esperado para cada consulta. En el cuadro ubicado en el extremo inferior de la ventana se mostrarán las consultas añadidas a la batería de casos de test hasta el momento

-   Puede seleccionar una o más de las opciones dispuestas en los checkbox que se encuentran en la parte inferior de la ventana para configurar el tipo de comparación entre los resultados esperados y los resultados obtenidos que se efectuará al momento de correr los casos de prueba:

    -   **Sin Orden**: compara los conjuntos de resultados esperados y obtenidos sin importar el orden de las respuestas (es decir, sin importar el orden en que fueron especificados en el archivo del casos de prueba, ni el orden en que se obtuvieron las respuestas al ejecutar las consultas en el intérprete de SWI-Prolog).
    -   **Primer Resultado**: solo compara el primer resultado esperado y el primer resultado obtenido, ignorando soluciones alternativas (es decir, se comparará el primer resultado especificado en el archivo de casos de prueba con el primer resultado obtenido por el intérprete de SWI-Prolog).

![image](https://github.com/user-attachments/assets/51888cad-390f-432b-8679-c3115086b7f1)

-   Observaciones adicionales:
    -   Si se seleccionan ambos checkbox, la ejecución del caso de test tendrá éxito si el primer resultado obtenido por el intérprete de SWI-Prolog al ejecutarlo está contenido dentro de los resultados esperados especificados en el caso de test.
    -   Si no se selecciona ninguno de los dos checkbox, la ejecución del caso de test tendrá éxito sí y solo sí los conjuntos de resultados esperados y obtenidos coinciden.
    -   De querer definir un caso de test negativo (es decir, una consulta cuyo resultado esperado es fallido, obteniendo False como respuesta del intérprete de SWI-Prolog), la selección de las opciones dispuestas en los checkbox no afectan al resultado. La ejecución del caso de test tendrá éxito sí y solo sí el resultado obtenido por el intérprete de SWI-Prolog es False.

2.  Escribir en el cuadro de texto ubicado en el extremo superior de la ventana (`Crear Query de Caso de Prueba`) la query a probar. Tener en cuenta que solo se puede ingresar una query a la vez.

![image](https://github.com/user-attachments/assets/929b4a36-2ea7-4515-af28-136dbaaf3f35)

> [!IMPORTANT]
> El modo de creación de casos de test manual permite agregar una query a la vez, y considerará incorrectas múltiples queries separadas por puntos.

3.  Escribir en el cuadro de texto ubicado en el medio de la ventana (`Resultado Esperado del Caso de Prueba`) el resultado que se espera que el intérprete de SWI-Prolog obtenga al ejecutar las queries especificadas en el punto anterior. Tener en cuenta las siguientes consideraciones sobre la sintaxis:

![image](https://github.com/user-attachments/assets/f955e75d-48c0-40f8-9c9c-9ba292e72198)

-   Si el resultado es verdadero sin ninguna unificación o falso, colocar True o False respectivamente.
-   Si el resultado es verdadero con unificaciones, colocar las variables como:

    -   Variable : Valor
    -   Múltiples variables en la misma respuesta deben estar separadas con ampersand (&)
    -   Múltiples conjuntos de unificaciones válidos separados por enter

-   Ejemplo:

    -   Resultado colocado:
        -   X : 2 & Lista : [2, 3, 4]
        -   X : 3 & Lista : [2, 3, 4]
        -   X : 4 & Lista : [2, 3, 4]
    -   Equivale a lo siguiente en el intérprete:
        -   X = 2, Lista = [2, 3, 4]
        -   X = 3, Lista = [2, 3, 4]
        -   X = 4, Lista = [2, 3, 4]

-   Es importante notar que la comparación de resultados esperados y obtenidos es usando la unificación de Prolog, excepto que dos variables libres son consideradas iguales.

4.  Acciones para la generación de la batería de tests:

    -   **Agregar**: incorpora a la batería de tests el caso de prueba recientemente definido. Luego de presionar este botón se visualizará en el panel inferior de la ventana la consulta recientemente incorporada a la batería.
    -   **Guardar**: permite almacenar la batería de tests generada hasta el momento (correspondientes a las consultas visualizadas en el panel inferior de la ventana) en un archivo.
    -   **Deshacer**: elimina el último caso de prueba de la batería de tests generada hasta el momento.
    -   **Limpiar**: elimina todos los caso de prueba de la batería de tests generada hasta el momento.

Luego de presionar **Agregar**

![image](https://github.com/user-attachments/assets/c5646aa9-2a3a-40df-aac0-dbd1d8c5799d)

5.  Una vez finalizado el añadido de casos de prueba a la batería de tests, presionar en **Guardar**.
6.  Elegir el archivo en donde se guardarán las consultas.

![image](https://github.com/user-attachments/assets/6e70c003-ae44-4ee3-9d3e-73f807f68580)

8.  Presionar en `Guardar` o `Save`.

### Creación de batería de tests asistido

Esta funcionalidad está solo disponible para la versión de profesores (`teacher_main.exe`), ya que requiere una correcta resolución al problema para crear la batería de tests.

1.  Presionar el botón **Cargar Base de Conocimiento**.

![image](https://github.com/user-attachments/assets/d8669330-aa1e-4119-b25f-39bcfb3dad85)

> [!IMPORTANT]
> Dado limitaciones actuales, para cargar una nueva base de conocimiento se requiere cerrar y abrir la aplicación

2.  Elegir el archivo de base de conocimiento de PROLOG.
3.  Presionar en `Abrir` u `Open`.

![image](https://github.com/user-attachments/assets/3bc1dec3-3f14-4f6a-b973-3f295ba6dc09)

4.  Presionar el botón **Crear Tests Asistido**.

![image](https://github.com/user-attachments/assets/d0a9472a-a753-4527-8ab6-ec3116ac923c)

5.  Escribir las consultas que conformarán los casos de prueba en el cuadro ubicado en el extremo superior de la ventana.

![image](https://github.com/user-attachments/assets/bcc3c64f-92e0-43cb-9036-243f5fe55d87)

> [!IMPORTANT]
> El modo de creación de casos de test asistido no requiere la especificación del resultado esperado para cada query. Los resultados esperados serán obtenidos a partir de la resolución de la consulta considerando la base de conocimiento cargada

-   En el cuadro ubicado en el extremo superior de la ventana deberá escribir las consultas que corresponden a los casos de test, y en el cuadro del medio deberá indicar el resultado esperado para cada consulta. En el cuadro ubicado en el extremo inferior de la ventana se mostrarán las consultas añadidas a la batería de casos de test hasta el momento

-   Puede seleccionar una o más de las opciones dispuestas en los checkbox que se encuentran en la parte inferior de la ventana para configurar el tipo de comparación entre los resultados esperados y los resultados obtenidos que se efectuará al momento de correr los casos de prueba:

    -   **Sin Orden**: compara los conjuntos de resultados esperados y obtenidos sin importar el orden de las respuestas (es decir, sin importar el orden en que fueron especificados en el archivo del casos de prueba, ni el orden en que se obtuvieron las respuestas al ejecutar las consultas en el intérprete de SWI-Prolog).
    -   **Primer Resultado**: solo compara el primer resultado esperado y el primer resultado obtenido, ignorando soluciones alternativas (es decir, se comparará el primer resultado especificado en el archivo de casos de prueba con el primer resultado obtenido por el intérprete de SWI-Prolog).

![image](https://github.com/user-attachments/assets/e6afc521-47d3-4104-8c7c-57f6aef2f5de)

-   Observaciones adicionales:
    -   Si se seleccionan ambos checkbox, la ejecución del caso de test tendrá éxito si el primer resultado obtenido por el intérprete de SWI-Prolog al ejecutarlo está contenido dentro de los resultados esperados especificados en el caso de test.
    -   Si no se selecciona ninguno de los dos checkbox, la ejecución del caso de test tendrá éxito sí y solo sí los conjuntos de resultados esperados y obtenidos coinciden.
    -   De querer definir un caso de test negativo (es decir, una consulta cuyo resultado esperado es fallido, obteniendo False como respuesta del intérprete de SWI-Prolog), la selección de las opciones dispuestas en los checkbox no afectan al resultado. La ejecución del caso de test tendrá éxito sí y solo sí el resultado obtenido por el intérprete de SWI-Prolog es False.

6.  Acciones para la generación de la batería de tests:

    -   **Agregar**: incorpora a la batería de tests el caso de prueba recientemente definido. Luego de presionar este botón se visualizará en el panel inferior de la ventana la consulta recientemente incorporada a la batería.
    -   **Guardar**: permite almacenar la batería de tests generada hasta el momento (correspondientes a las consultas visualizadas en el panel inferior de la ventana) en un archivo.
    -   **Deshacer**: elimina el último caso de prueba de la batería de tests generada hasta el momento.
    -   **Limpiar**: elimina todos los caso de prueba de la batería de tests generada hasta el momento.

Luego de presionar **Agregar**

![image](https://github.com/user-attachments/assets/323e9628-5386-4796-8542-9c5693e51eaa)

7.  Una vez finalizado el añadido de casos de prueba a la batería de tests, presionar en **Guardar**.

![image](https://github.com/user-attachments/assets/9837f581-8fe2-4dbe-b4a6-fafb6624c916)

8.  Elegir el archivo en donde se guardarán las consultas.

![image](https://github.com/user-attachments/assets/9c8f1b86-7849-470f-aa5f-b3c995bdc1fb)

9.  Presionar en `Guardar` o `Save`.

## Utilización de la versión de consola

Para probar por consola se tiene que llamar al ejecutable de consola (`console_main.exe`) con los siguientes argumentos:

> [!NOTE]
> Para especificar una direccion que incluya espacios, rodee la dirección con comillas dobles (Ejemplo: `"archivos de prolog/base.pl`). Permite direcciones relativas y absolutas.

-   Primer argumento: la dirección del archivo .pl correspondiente a la de base de conocimiento en PROLOG.
-   Segundo argumento en adelante: dirección de los archivos o carpetas de batería de tests
    -   Los archivos tienen que tener terminación .json
    -   De cada carpeta ingresada se buscará archivos .json en esa carpeta, sin buscar en dentro de carpetas dentro.
-   Se tiene que escribir el nombre completo del archivo, incluyendo extensión (`.pl` para bases de conocimiento y `.json` para baterías de test).
-   Ejemplo:
    -   Estando en una consola en la carpeta de la herramienta: - `console_main.exe test_files/test_knowledge_base.pl test_files/test_examples.json test_files/test_examples_ordered.json`

![image](https://github.com/user-attachments/assets/ea2b6732-9958-43e6-9f99-5482abaf4d49)

