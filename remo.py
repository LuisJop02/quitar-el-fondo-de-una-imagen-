import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import rembg

def quitar_fondo(ruta_imagen):
    # Abrir la imagen
    with open(ruta_imagen, "rb") as f:
        imagen = f.read()
    
    # Quitar el fondo
    imagen_sin_fondo = rembg.remove(imagen)
    
    return imagen_sin_fondo

def seleccionar_imagen():
    # Abrir el diálogo para seleccionar la imagen
    ruta_imagen = filedialog.askopenfilename()
    # Quitar el fondo de la imagen
    imagen_sin_fondo = quitar_fondo(ruta_imagen)
    # Obtener el nombre del archivo
    nombre_archivo = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    # Guardar la imagen sin fondo
    guardar_imagen(imagen_sin_fondo, nombre_archivo)

def guardar_imagen(imagen, nombre_archivo):
    if nombre_archivo:
        # Guardar la imagen sin fondo con el nombre especificado
        with open(nombre_archivo, "wb") as f:
            f.write(imagen)
        print("Imagen sin fondo guardada correctamente como:", nombre_archivo)

# Crear una ventana
ventana = tk.Tk()
ventana.title("Quitar Fondo de Imagen")

# Botón para seleccionar imagen
boton = tk.Button(ventana, text="Seleccionar Imagen", command=seleccionar_imagen)
boton.pack(pady=10)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()

