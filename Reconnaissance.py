import cv2
import numpy as np

# charger le fichier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Démarrer la Webcam
cap = cv2.VideoCapture(0)

while True:
    # Verifier l'image à partir de la Webcam
    ret, frame = cap.read()

    # 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Détecter les visages dans le cadre
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Faire un tableau autour de tous les visages détectés
    for (x, y, w, h) in faces:
        # Extract the face ROI
        face_roi = gray[y:y+h, x:x+w]

        # Recognize le visage
        

        # Dessiner la zone de délimitation du visage autour visage avec le nom et le "status" de la personne
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(frame, 'Name:, status:', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

    
    cv2.imshow('Visage', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
