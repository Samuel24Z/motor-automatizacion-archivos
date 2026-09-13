import os # os nos permite interactuar con el sistema operativo, en este caso usaremos os.path para interactuar con rutas del sistema de archivos
import shutil # este módulo nos permite realizar operaciones sobre archivos y conjuntos de archivos
import getpass

from tkinter import Tk, filedialog
from datetime import datetime

usuario = getpass.getuser() # Se captura al usuario que se logueo a la máquina y que está usando este programa

ventana = Tk() # creamos una ventana
ventana.withdraw() # nos ayuda a quitar la ventana de cmd que aparece con la ventana de selección del archivo

rutaTrabajo = filedialog.askdirectory(title="Seleccionar carpeta") # obtenemos el directorio y le damos un nombre a la ventana

extensiones = { # Creamos el diccionario que contiene la extsensiones
    ".jpg" : "Imagenes",
    ".png" : "Imagenes",
    ".pdf" : "PDFs",
    ".mp4" : "Videos",
    ".odt": "Documentos_Writer",
    ".txt"  : "Documentos_txt"
}

# Bucle for para la creación de carpetas
for carpeta in set(extensiones.values()):
    rutaCarpeta = os.path.join(rutaTrabajo, carpeta) # join une la ruta con el nombre de la carpeta
    
    if not os.path.exists(rutaCarpeta): # si no existe una carpeta con el nombre especificado
        os.makedirs(rutaCarpeta) # entonces se crea la carpeta

# Bucle for para recorrer la carpeta que contiene todos los acrhivos revueltos y moverlos a sus carpetas respectivas
for archivo in os.listdir(rutaTrabajo):
    rutaArchivo = os.path.join(rutaTrabajo, archivo) # Se une la ruta del archivo con el nombre del mismo

    if os.path.isfile(rutaArchivo):
        nombre, ext = os.path.splitext(archivo) # Separa el nombre del archivo de su extensión
        ext = ext.lower() #deja en minúsculas todas las extensiones en caso de que haya algunas con mayúsculas

        if ext in extensiones: # si la extensión obtenida está en el diccionario de extensiones
            destino = os.path.join(rutaTrabajo, extensiones[ext], archivo) # Se une la ruta con el nombre de carpeta proveniente de la colección extensiones y luego esto se une con el nombre del archivo
            shutil.move(rutaArchivo, destino)

            with open(os.path.join(rutaTrabajo, "log_movimientos.txt"), "a", encoding="utf-8") as log: # Creamos un bloque with y con el manejamos un objeto llamdo "log"
                log.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Usuario: {usuario}  - Archivo: {archivo} movido a  {destino}\n") # Escribimos la fecha y hora en que se movió así como el destino al que se movió

                
'''
Fuentes de información
https://docs.python.org/3/library/os.html
https://docs.python.org/3/library/os.path.html#module-os.path
https://docs.python.org/es/3/library/shutil.html#module-shutil
'''



