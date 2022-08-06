import cv2
import numpy as np
import os
import pygame
import time
import HandTrackingModule as htm

# OpenCV & Mediapipe tracking
pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = htm.handDetector(detectCon=0.85)


# Pygame
pygame.init()
background_color = (255,255,255)
(width, height) = (1280,720)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Game")
screen.fill(background_color)
pygame.display.flip()

handPointing = pygame.image.load("assets/1.png")
handPointing = pygame.transform.scale(handPointing, (40, 40))



running = True

while running:

    success, img = cap.read()
    img = cv2.flip(img, 1)
    img.flags.writeable = False
    img = detector.findHands(img, draw=False)
    lmList = detector.findPosition(img)
    x1, y1 = 0, 0
    isDrawing = False
    if len(lmList) != 0:
        # index finger coord
        x1, y1 = lmList[8][1:]

        # Middle finger coord
        # x2, y2 = lmList[12][1:]

        # Return an array [0,0,0,0,0] each element is a finger, 0 is close and 1 is up
        fingers = detector.fingersUp()

        # 2 finger up (index and middle)
        if fingers[1] and fingers[2]:
            print("Select")

        # 1 finger up (index)
        if fingers[1] and fingers[2] == False:
            print("Draw")
            isDrawing = True

        # Hand close
        if all(finger == False for finger in fingers):
            print("Close")

        # index_up = lmList[8][2] < lmList[6][2]
        # index_down = lmList[8][2] > lmList[6][2]
        # middle_up = lmList[12][2] < lmList[10][2]
        # middle_down = lmList[12][2] > lmList[10][2]
        # ring_up = lmList[16][2] < lmList[14][2]
        # ring_down = lmList[16][2] > lmList[14][2]
        # little_up = lmList[20][2] < lmList[18][2]
        # little_down = lmList[20][2] > lmList[18][2]
        # thumb_up = lmList[4][1] < lmList[2][1]
        # thumb_down = lmList[4][1] > lmList[2][1]
        #
        # if thumb_down and index_up and middle_up and ring_down and little_down:
        #     print("Select")
        #
        # if thumb_down and index_up and middle_down and ring_down and little_down:
        #     print("Draw")
        #     isDrawing = True
        #
        # if thumb_up and index_up and middle_down and ring_down and little_down:
        #     print("Change")
        #
        # if thumb_down and index_down and middle_down and ring_down and little_down:
        #     print("Close")

    # Show opencv window

    # fps indicator
    # cTime = time.time()
    # fps = 1 / (cTime - pTime)
    # pTime = cTime

    # img.flags.writeable = True
    # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    #
    # cv2.imshow("Image", img)

    cv2.waitKey(1)

    # Pygame
    screen.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if isDrawing:
        screen.blit(handPointing, (x1, y1))
    pygame.display.update()
cap.release()
pygame.quit()
