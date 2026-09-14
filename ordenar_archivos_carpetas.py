import os # os nos permite interactuar con el sistema operativo, en este caso usaremos os.path para interactuar con rutas del sistema de archivos
import shutil # este módulo nos permite realizar operaciones sobre archivos y conjuntos de archivos
import getpass
from pathlib import Path

from tkinter import Tk, filedialog
from datetime import datetime

usuario = getpass.getuser() # Se captura al usuario que se logueo a la máquina y que está usando este programa

procesados = 0
movidos = 0
errores = 0

def seleccionarCarpeta():
    ventana = Tk() # creamos una ventana
    ventana.withdraw() # nos ayuda a quitar la ventana de cmd que aparece con la ventana de selección del archivo

    rutaRaiz = filedialog.askdirectory(title="Seleccionar carpeta") # obtenemos el directorio y le damos un nombre a la ventana

    if not rutaRaiz:
        return
    else:
        return rutaRaiz

extensiones = { # Creamos el diccionario que contiene la extsensiones
    ".jpg" : "Imagenes",
    ".png" : "Imagenes",
    ".pdf" : "PDFs",
    ".mp4" : "Videos",
    ".odt": "Documentos_Writer",
    ".txt"  : "Documentos_txt"
}

rutaTrabajo = seleccionarCarpeta()
if not rutaTrabajo:
    errores += 1
    print("No se eligió ninguna ruta para ordenar archivos")
else:
    # Bucle for para la creación de carpetas
    for carpeta in set(extensiones.values()):
        rutaCarpeta = os.path.join(rutaTrabajo, carpeta) # join une la ruta con el nombre de la carpeta
        
        if not os.path.exists(rutaCarpeta): # si no existe una carpeta con el nombre especificado
            os.makedirs(rutaCarpeta) # entonces se crea la carpeta

    # Bucle for para recorrer la carpeta que contiene todos los acrhivos revueltos y moverlos a sus carpetas respectivas
    for archivo in os.listdir(rutaTrabajo):
        if "log" in archivo:
            rutaConNombre = os.path.join(rutaTrabajo, archivo)
            errores += 1
            procesados += 1
            with open(os.path.join(rutaTrabajo, "log_errores.txt"), "a", encoding="utf-8") as log: # Creamos un bloque with y con el manejamos un objeto llamdo "log"
                log.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Usuario: {usuario} - Error en {rutaConNombre}, los logs de procesamiento no pueden moverse fuera del directorio raíz\n") # Escribimos la fecha y hora en que se movió así como el usuario que lo movio y la descripción del error
        else:
            rutaArchivo = os.path.join(rutaTrabajo, archivo) # Se une la ruta del archivo con el nombre del propio archivo

        if os.path.isfile(rutaArchivo):
            nombre, ext = os.path.splitext(archivo) # Separa el nombre del archivo de su extensión
            ext = ext.lower() #deja en minúsculas todas las extensiones en caso de que haya algunas con mayúsculas

            if ext in extensiones: # si la extensión obtenida está en el diccionario de extensiones
                # Se obtiene la fecha de la última modificación con getmtime()
                fechaUltimaModificacion = datetime.fromtimestamp(os.path.getmtime(rutaArchivo))
                subcarpetaFecha = fechaUltimaModificacion.strftime("%Y-%m") # Le damos formato a la fecha usando solo mes y dia

                carpetaTipoArchivo = os.path.join(rutaTrabajo, extensiones[ext])
                # Se crea la ruta C:\Users\Usuario\MiProyecto\TipoArchivo\Año-mes
                carpetaFecha = os.path.join(carpetaTipoArchivo, subcarpetaFecha)

                # Si no existe la carpeta entonces se crea
                if not os.path.exists(carpetaFecha):
                    os.makedirs(carpetaFecha)

                # Se une toda la ruta C:\Users\Usuario\MiProyecto\TipoArchivo\Año-mes con el nombre del archivo
                destino = os.path.join(carpetaFecha, archivo)
                destino2 = Path(destino)

                if not destino2.exists: # Si el archivo no existe
                    shutil.move(rutaArchivo, destino)

                    with open(os.path.join(rutaTrabajo, "log_movimientos.txt"), "a", encoding="utf-8") as log: # Creamos un bloque with y con el manejamos un objeto llamdo "log"
                        log.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Usuario: {usuario}  - Archivo: {archivo} movido a {destino}\n") # Escribimos la fecha y hora en que se movió así como el usuario que lo movio y el destino al que se movió

                    movidos += 1
                    procesados += 1                        
                else: # Si el archivo ya existe
                    errores += 1
                    procesados += 1

                    with open(os.path.join(rutaTrabajo, "log_errores.txt"), "a", encoding="utf-8") as log: # Creamos un bloque with y con el manejamos un objeto llamdo "log"
                        log.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Usuario: {usuario} - Error: {archivo} ya existe, no se movio al destino especificado\n") # Escribimos la fecha y hora en que se movió así como el usuario que lo movio y la descripción del error

                print("Procesados:", + procesados)
                print("Movidos:", + movidos)
                print("Errores:", + errores)
                
'''
Fuentes de información
https://docs.python.org/3/library/os.html
https://docs.python.org/3/library/os.path.html#module-os.path
https://docs.python.org/es/3/library/shutil.html#module-shutil
'''



