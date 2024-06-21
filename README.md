# Reconnaissence_Faciale
Explication détaillée :
Importation des bibliothèques :
import cv2
import numpy as np

* cv2 : bibliothèque OpenCV pour la vision par ordinateur.
* numpy : bibliothèque pour le calcul numérique en Python, souvent utilisée avec OpenCV.

Chargement du classificateur Haar pour la détection des visages :
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

* cv2.CascadeClassifier : charge le classificateur en cascade pour détecter les visages.
* cv2.data.haarcascades : chemin vers les fichiers Haar cascade fournis avec OpenCV.

Initialisation de la webcam :
cap = cv2.VideoCapture(0)

* cv2.VideoCapture(0) : ouvre la webcam par défaut (index 0).

Boucle principale :
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

* cap.read() : lit une frame de la webcam.
* cv2.cvtColor : convertit la frame en niveaux de gris.
* detectMultiScale : détecte les visages dans l'image en niveaux de gris.

Traitement des visages détectés:
for (x, y, w, h) in faces:
    face_roi = gray[y:y+h, x:x+w]
    # label, confidence = recognizer.predict(face_roi)
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.putText(frame, 'Name: fellipe, status: étudiant', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

* Boucle à travers chaque visage détecté.
* face_roi : extrait la région d'intérêt (ROI) du visage pour la reconnaissance (section commentée).
* cv2.rectangle : dessine un rectangle autour du visage.
* cv2.putText : affiche le texte au-dessus du rectangle.

Affichage et sortie :
cv2.imshow('Visage', frame)
if cv2.waitKey(1) & 0xFF == ord('q'):
    break

* cv2.imshow : affiche la frame avec les annotations.
* cv2.waitKey : attend l'appui d'une touche; sort de la boucle si 'q' est pressé.

Libération des ressources:
cap.release()
cv2.destroyAllWindows()

* cap.release : libère la webcam.
* cv2.destroyAllWindows : ferme toutes les fenêtres OpenCV ouvertes.
