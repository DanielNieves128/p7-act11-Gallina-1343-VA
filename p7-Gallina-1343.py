# Daniel Nieves NC=1343
import os
import sys

# 1. Intentar importar librerías con manejo de error
try:
    import cv2
    import matplotlib.pyplot as plt
except ModuleNotFoundError as e:
    print(f"❌ Error de librerías: {e}")
    print("Ejecuta en la terminal: python -m pip install opencv-python matplotlib")
    sys.exit(1)

# 2. Definir nombre de la imagen y verificar que exista en disco
nombre_imagen = 'Gallina.png'

if not os.path.exists(nombre_imagen):
    print(f"❌ Error: No se encontró el archivo '{nombre_imagen}' en la ruta actual:")
    print(f"   Ruta actual: {os.getcwd()}")
    print("   Verifica que la imagen esté en la misma carpeta que este script.")
    sys.exit(1)

# 3. Cargar imagen desde disco (OpenCV la lee en formato BGR)
img_bgr = cv2.imread(nombre_imagen)

if img_bgr is None:
    print(f"❌ Error: OpenCV no pudo leer el archivo '{nombre_imagen}'. Verifica que el formato o el archivo no esté dañado.")
    sys.exit(1)

# 4. Conversiones de color
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# 5. Mostrar los resultados comparativos
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].imshow(img_bgr)
axes[0].set_title("Original en OpenCV (BGR incorrecto)")

axes[1].imshow(img_rgb)
axes[1].set_title("Convertido a RGB")

axes[2].imshow(img_gray, cmap='gray')
axes[2].set_title("Escala de Grises")

for ax in axes:
    ax.axis('off')

plt.tight_layout()
plt.show()

print("Daniel Nieves NC=1343")