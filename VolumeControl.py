import time
import cv2
import numpy as np
import HandTrackingModule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# init volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

# determines the range of volume on the device
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]

# init vars 
vol = 0
wCam, hCam = 640, 460

# set up camera

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)

    prev_t = 0
    detector = htm.handDetector()
    volBar = 400
    volPer = 0

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        landmarks = detector.findPosition(img, draw=False)

        if landmarks:
            # determine position of thumb and index finger as well as needed values
            x1, y1 = landmarks[4][1], landmarks[4][2]
            x2, y2 = landmarks[8][1], landmarks[8][2]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            cv2.circle(img, (x1,y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2,y2), 15, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1,y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            length = math.hypot(x2-x1, y2-y1) # input to change certain functions
            
            vol = np.interp(length, [50, 200], [minVol, maxVol]) # will convert the length range to volumne range
            volBar = np.interp(length, [50, 200], [400, 150]) # will convert the length range to the volume bar range
            volPer = np.interp(length, [50, 200], [0, 100]) # will convert the length range to the volume bar range
            volume.SetMasterVolumeLevel(vol, None)

            if length < 50:
                cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
            
        # draw volumne bar 
        cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f"Volume: {int(volPer)}%", (40,450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

        # set up fps counter
        curr_t = time.time()
        fps = 1/(curr_t - prev_t)
        prev_t = curr_t
        cv2.putText(img, f"FPS: {fps}", (50,70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()