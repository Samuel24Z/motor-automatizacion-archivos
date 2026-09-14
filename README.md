# Motor de procesamiento automatizado de archivos
## Descripción general
Este proyecto tiene por finalidad el ordenamiento y clasificación automatizado de archivos guardados en el disco duro de la computadora, para esto se va utilizar Python junto con sus diversas bibliotecas de interacción con el sistema, gestión de archivos y manipulación de fechas. De manera más específica este proyecto va organizar un conjunto desordenado de archivos por tipo o extensión además de ordenarlos por fecha para cada conjunto de archivos del mismo tipo.

Este proyecto tiene las siguientes etapas:
* Obtención de ruta con archivos a ordenar
* Uso de estrucuras repetitivas para crear los directorios de cada tipo de archivo
* Uso de estrucuras repetitivas para organizar los archivos por fecha
* Operación de traslado de archivos desde su origen hacia un destino clasificado
* Creación de logs para registrar errores y movimientos éxitosos en las operaciones.
* Manejo de posibles errores durante el flujo de ejecución del programa

## Archivos de registros de eventos
Este programa crea dos archivos de registros de eventos, estos se describen a continuación.
* Resgitro de movimientos: Este contiene la fecha y hora en que ocurrió el movimiento de un archivo hacia su destino ya clasificado, el nombre del usuario que actualmente tiene la sesión abierta en el sistema operativo y que está ejecutando el programa, el nombre el propio archivo y la ruta hacia la que fue movido tal archivo.
* Registro de errores: Este archivo almacena una lista de los diferentes incidentes que puede manejar el programa tal como la sobrescritura de un archivo que previamente ya fue clasificado y la preservación de la misma ruta de guardado de los propios archivos de registro, esto último tiene como objetivo que los archivos de registro sean clasificados como archivos que se tienen que ordenar.

## Ejemplos de implementación
La siguiente imagen muestra el arbol de archivos que se desea ordenar.

![Arbol original de archivos](/Imagenes/arbol_original_archivos.png)

Ahora bien, el conjunto de archivos que se ordeno se muestra en el árbol de la siguiente imagen.

![Arbol ordenado de archivos](/Imagenes/arbol_modificado_archivos.png)

En la siguiente figura se muestra la ejecución del programa por medio de línea de comandos, en esta ejecución no ocurrió ningún error de procesamiento.

![Ejecución sin errores](/Imagenes/ejecucion_inicial.png)

Adicionalmente, en la siguiente figura se muestra una ejecución con dos errores, el pimero es ocasioando porque se intenta mover un archivo que previamente ya estaba en las carpetas organizadas y el otro error es originado porque se intenta mover un archivo de registros pero estos solamente se deben quedar en la carpeta raíz de donde se organizaron los archivos.

![Ejecución con errores](/Imagenes/ejecucion_errores.PNG)







