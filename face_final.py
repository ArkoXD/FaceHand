import cv2
import face_recognition

def detect_face(framergb):
    face_locations = face_recognition.face_locations(framergb)
    for y1, x1, y2, x2 in face_locations:
        return [(x2, y2), (x1, y1)]
