
from rembg import remove # descargas la libreria 
from PIL import Image # te permite manipular la imagen 



image_input= Image.open() #ingresas la direccion de imagen que deseas quitar le fondo 
output = remove(image_input)
output.save("")   # ingresas el nombre de como deseas aguardarlo  