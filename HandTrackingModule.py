

import cv2
import mediapipe as mp


class handDetector():
    def __init__(self, mode=False, maxHands=1, detectCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectCon = detectCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectCon,
                                        min_tracking_confidence=self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.mpDrawingStyle = mp.solutions.drawing_styles
        self.tipIds = [4, 8, 12, 16, 20]
        self.handType = 'None'
        self.handState = 'Resting'
        # Video capture
        # self.pTime = 0
        # self.cTime = 0
        # capture = cv2.VideoCapture(0)
        # capture.set(3, 1280)
        # capture.set(4, 720)

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for hand in self.results.multi_handedness:
                self.handType = hand.classification[0]
                # print(self.handType.label)
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS,
                                               self.mpDrawingStyle.get_default_hand_landmarks_style(),
                                               self.mpDrawingStyle.get_default_hand_connections_style())
        return img
    def findPosition(self, img, handNo = 0, handL = 8, draw = True):
        self.lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):

                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                self.lmList.append([id, cx, cy])

                if draw and id == handL:
                    cv2.circle(img, (cx, cy), 25, (255,0,255), cv2.FILLED)
                    cv2.putText(img,(self.handState + "-" + self.handType.label), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        return self.lmList

    def fingersUp(self):
        fingers = []

        # Thumb
        if self.handType.label == "Right":
            if self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        if self.handType.label == "Left":
            if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Other fingers
        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

    #Get current hand state by checking the finger array
    def getHandState(self):
        self.handState = 'Unmapped'
        if self.results.multi_hand_landmarks:
            fingers = self.fingersUp()
            if fingers[1] and fingers[2] and not fingers[3] and not fingers[4]:
                self.handState = "Selecting"
                return self.handState
            if fingers[1] and not fingers[2] and not fingers[3] and not fingers[4]:
                self.handState = "Drawing"
                return self.handState

        return self.handState