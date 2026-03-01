from PIL import Image
from rembg import remove

path_in = r"C:\Users\alexi\OneDrive\Documentos\VS2DAW_ANDREA\PCP\ManipulacionImagenes\FreddyMercury.png"
path_out = r"C:\Users\alexi\OneDrive\Documentos\VS2DAW_ANDREA\PCP\ManipulacionImagenes\FreddyMercury_sinFondo.png"

# Abrimos la imagen y le asignamos a una variable
foto = Image.open(path_in)

# Aplicamos la función para eliminar el fondo y guardamos el resultado en la ruta de salida
salida = remove(foto)
salida.save(path_out)