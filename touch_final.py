import cv2
import face_final as f
import hands_final as h

def rectangles_intersect(rect1, rect2):
    [(x21, y21), (x11, y11)] = rect1
    [(x22, y22), (x12, y12)] = rect2
    if ((x21 <= x22 and x21 >= x12) or (x11 <= x22 and x11 >= x12)) and ((y21 <= y22 and y21 >= y12) or (y11 <= y22 and y11 >= y12)):
        return True
    return False

video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    capture, frame = video_capture.read()

    if not capture:
        print("Error: Could not receive frame. Exiting...")
        break

    framergb = frame[:, :, ::-1]

    face_coordinates = f.detect_face(framergb)
    hand_coordinates = h.detect_hands(framergb)
    if face_coordinates:
        cv2.rectangle(frame, face_coordinates[0], face_coordinates[1], (0, 255, 0), 2)

    if hand_coordinates:
        cv2.rectangle(frame, hand_coordinates[0], hand_coordinates[1], (0, 255, 0), 2)
    

    if face_coordinates and hand_coordinates:
        if rectangles_intersect(face_coordinates, hand_coordinates):
            cv2.putText(frame, 'hands and face touching!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()