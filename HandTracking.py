import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0) # init camera

# creating hands object
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB) # process img from opencv 

    # extract each hand
    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, hand)
