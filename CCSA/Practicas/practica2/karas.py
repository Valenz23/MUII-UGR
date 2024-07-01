# casa 9zzKluv41142 

import cv2
import requests
import numpy as np

# Cargamos el clasificador pre-entrenado para la detección de caras
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Función para cargar una imagen desde una URL
def load_image_from_url(url):
    response = requests.get(url)
    img_array = np.array(bytearray(response.content), dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return img

# Función para detectar caras y dibujar un marco alrededor de ellas
def detect_faces(image_url):
    # Cargamos la imagen desde la URL
    img = load_image_from_url(image_url)

    if img is None:
        print("No se pudo cargar la imagen desde la URL.")
        return None

    # Convertimos la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detectamos caras en la imagen
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Dibujamos un marco alrededor de las caras detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)

    return img

# Llamamos a la función de detección de caras con la URL de la imagen como argumento
detected_image = detect_faces('https://c8.alamy.com/compes/2wann4w/sonrie-corbata-y-union-de-padre-con-el-nino-en-la-sala-de-estar-de-la-casa-de-la-familia-juntos-por-amor-feliz-cuidado-y-papa-hablando-o-hablando-con-nina-nina-con-2wann4w.jpg')

if detected_image is not None:
    cv2.imwrite("faces_detected.jpg", detected_image)
    print("Imagen con las caras detectadas guardada como 'faces_detected.jpg'")


###################################################################################

# import cv2
# import requests
# import numpy as np
# import json

# # Cargamos el clasificador pre-entrenado para la detección de caras
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # Función para cargar una imagen desde una URL
# def load_image_from_url(url):
#     response = requests.get(url)
#     img_array = np.array(bytearray(response.content), dtype=np.uint8)
#     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#     return img

# # Función para detectar caras y dibujar un marco alrededor de ellas
# def detect_faces(image_url):
#     # Cargamos la imagen desde la URL
#     img = load_image_from_url(image_url)

#     if img is None:
#         return {"error": "No se pudo cargar la imagen desde la URL."}

#     # Convertimos la imagen a escala de grises
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Detectamos caras en la imagen
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#     # Dibujamos un marco alrededor de las caras detectadas
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)

#     # Convertimos la imagen con las caras detectadas a base64
#     retval, buffer = cv2.imencode('.jpg', img)
#     img_base64 = buffer.tobytes()

#     return {"image_base64": img_base64}

# # Función de entrada para OpenFaaS
# def handle(req):
#     try:
#         req_json = json.loads(req)
#         image_url = req_json["image_url"]
#         result = detect_faces(image_url)
#         return json.dumps(result)
#     except Exception as e:
#         return json.dumps({"error": str(e)})

