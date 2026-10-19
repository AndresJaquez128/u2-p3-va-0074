import os
import cv2

# 1. Ruta y carga
ruta = os.path.join("img-original-0074", "batidora.jpg")
# imagen
# vamos a crear nuestra matriz principal
batidora = cv2.imread(ruta)
# print(batidora) muestra las matrices de la imagen
batidora1 = cv2.cvtColor(batidora, cv2.COLOR_BGR2RGB)
# convertir de BGR a RGB color rojo COLOR_BGR2RGB
# 2. Imprimir matriz y mostrar en ventana de OpenCV
print(batidora)
cv2.imshow("Batidora color0074", batidora1)
cv2.waitKey(0) # tiempo de espera
cv2.destroyAllWindows() # destruye todas las ventanas en memoria