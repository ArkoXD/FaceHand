import cv2
import mediapipe as mp

mphands = mp.solutions.hands
hands = mphands.Hands()
def detect_hands(framergb):
    result = hands.process(framergb)
    h, w, c = framergb.shape
    hand_landmarks = result.multi_hand_landmarks
    if hand_landmarks:
        for handLMs in hand_landmarks:
            x_max = 0
            y_max = 0
            x_min = w
            y_min = h
            for lm in handLMs.landmark:
                x, y = int(lm.x * w), int(lm.y * h)
                if x > x_max:
                    x_max = x
                if x < x_min:
                    x_min = x
                if y > y_max:
                    y_max = y
                if y < y_min:
                    y_min = y
            return [(x_max, y_max), (x_min, y_min)]