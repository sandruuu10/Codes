import os
import shutil
from tqdm import tqdm

def clasificar_fotos(directorio_origen):
    # Directorios de destino
    nombre_carpeta_padre = os.path.basename(directorio_origen)

    directorio_destino_termografia = os.path.join(directorio_origen,  f'{nombre_carpeta_padre}_Termal')
    directorio_destino_visible = os.path.join(directorio_origen,  f'{nombre_carpeta_padre}_Wide')
    directorio_destino_zoom = os.path.join(directorio_origen,  f'{nombre_carpeta_padre}_Zoom')

    # Crear directorios de destino si no existen
    os.makedirs(directorio_destino_termografia, exist_ok=True)
    os.makedirs(directorio_destino_visible, exist_ok=True)
    os.makedirs(directorio_destino_zoom, exist_ok=True)

    # Iterar sobre cada archivo y clasificarlo
    for archivo in tqdm(os.listdir(directorio_origen), desc='Clasificando fotos'):
        if archivo.endswith('_T.JPG'):
            # Mover el archivo al directorio de destino para las fotos termografía
            shutil.move(os.path.join(directorio_origen, archivo), directorio_destino_termografia)
        elif archivo.endswith('_V.JPG') or archivo.endswith('_W.JPG'):
            # Mover el archivo al directorio de destino para las fotos visibles
            shutil.move(os.path.join(directorio_origen, archivo), directorio_destino_visible)
        elif archivo.endswith('_Z.JPG'):
         # Mover el archivo al directorio de destino para las fotos zoom
            shutil.move(os.path.join(directorio_origen, archivo), directorio_destino_zoom)

    # Eliminar la carpeta "Zoom" si está vacía
    if not os.listdir(directorio_destino_zoom):
        os.rmdir(directorio_destino_zoom)

if __name__ == '__main__':
    # Directorio de origen que contiene las fotos
    directorio_origen = os.getcwd()  # o especifica la ruta completa aquí

    # Clasificar las fotos
    clasificar_fotos(directorio_origen)

    input("Presiona Enter para salir...")


