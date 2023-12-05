import cv2
import numpy as np

# Cargar la imagen de la factura
image = cv2.imread(r"C:\Users\ralva\Universidad\factura.jpg")

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar un filtro de suavizado para reducir el ruido
smooth = cv2.GaussianBlur(gray, (5, 5), 0)

# Detectar los bordes en la imagen
edges = cv2.Canny(smooth, 100, 200)

# Encontrar los contornos en la imagen
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Encontrar el contorno más grande
largest_contour = max(contours, key=cv2.contourArea)

# Obtener los puntos del contorno
points = largest_contour.reshape(-1, 2)

# Agregar una caja alrededor del contorno
cv2.rectangle(image, (points[0][0], points[0][1]), (points[-1][0], points[-1][1]), (0, 255, 0), 2)

# Obtener los puntos de las esquinas de la caja
corners = np.array([[points[0][0], points[0][1]], [points[-1][0], points[-1][1]], [points[-1][0], points[0][1]], [points[0][0], points[-1][1]]], dtype=np.float32)

# Convertir las esquinas de la caja a coordenadas relativas
relative_corners = corners - points[0]

# Obtener el ancho y la altura de la caja
width = np.linalg.norm(relative_corners[0] - relative_corners[1])
height = np.linalg.norm(relative_corners[2] - relative_corners[3])

# Agregar un cuadro de texto en la caja
cv2.putText(image, "Formulario de factura", (int(points[0][0] + width / 2), int(points[0][1] + height / 2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
# Guardar la imagen
cv2.imwrite("factura_formulario.jpg", image)

