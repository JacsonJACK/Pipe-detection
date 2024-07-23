
#installed numpy-2.0.0 opencv-python-4.10.0.84

import cv2
import numpy as np

# Defina o caminho da imagem
image_path = r'C:/Users/SpeCtron/Downloads/Pipes/image022.jpg'

# Leia a imagem no modo colorido
img = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Verifique se a imagem foi carregada com sucesso
if img is None:
    print("Error opening image:", image_path)
    exit()

# Converta a imagem em tons de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar desfoque (opcional, ajuste o tamanho do kernel, se necessário)
gray_blurred = cv2.blur(gray, (3, 3))  # You can adjust the kernel size here (e.g., (5, 5))

# Detectar círculos usando a Hough transform
detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=1, maxRadius=40)

# Desenhe círculos detectados (se houver)
if detected_circles is not None:
    # Supondo que os círculos estejam em detected_circles[0] e cada círculo é uma lista com (x, y, r)
    círculos = detected_circles[0]  # Supondo que os círculos estejam em detected_circles[0]
    for pt in circles:
        x, y, r = pt[0], pt[1], pt[2]  # Assumindo coordenadas centrais nos índices 0 and 1, raio no índice 2

        # Certifique-se de que x e y sejam números inteiros antes de passar para cv2.circle
        x_int = int(x)
        y_int = int(y)

        # Converta o raio em inteiro e verifique seu valor
        r_int = int(r)
        print("Center:", (x_int, y_int), "Radius:", r_int)

        # Desenhe o círculo com o raio inteiro convertido
        cv2.circle(img, (x_int, y_int), r_int, (0, 255, 0), 2)
        cv2.circle(img, (x_int, y_int), 1, (0, 0, 255), 3)

# Exibir a imagem com círculos detectados
cv2.imshow("Detected Circles", img)

# Aguarde um pressionamento de tecla para fechar a janela
cv2.waitKey(0)

# Feche todas as janelas
cv2.destroyAllWindows()
