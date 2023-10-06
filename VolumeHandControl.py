import cv2
import time
import numpy as np
import HandTrackingModule as htm

# Define a resolução da câmera
wCam, hCam = 640, 480

# Inicializa a câmera
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Inicializa o tempo anterior
pTime = 0

# Inicializa o detector de mãos
detector = htm.handDetector(detectionCon=int(1))

while True:
  # Lê o frame da câmera
  success, img = cap.read()

  #espelha a camera
  img = cv2.flip(img, 1)

  # Encontra as mãos na imagem e mostra o "esqueleto"
  img = detector.findHands(img, draw=True)

  # Calcula o FPS
  cTime = time.time()
  fps = 1 / (cTime - pTime)
  pTime = cTime

  # Mostra o FPS na imagem
  cv2.putText(img, f'FPS: {int(fps)}', (20, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

  # Mostra a imagem na tela
  cv2.imshow("Img", img)

  # Aguarda a tecla ser pressionada
  cv2.waitKey(1)