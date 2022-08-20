import ball
import pygame
import pymunk
import pymunk.util as u
from pymunk import Vec2d
import HandTrackingModule as htm
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = htm.handDetector(detectCon=0.85)

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 900, 500
RAD = 20
LINE_WEIGHT = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")
space = pymunk.Space()
space.gravity = (0, 981)

FPS = 30
VEL = 5
DT = 1 / FPS


def create_segments(previouspos, currentpos):
    # The drawing function will draw a line from 2 point
    if previouspos == (0, 0): # if the pen is not inside the canvas or first start the app
         previouspos = currentpos # pass the current coordinate of the pen
    # draw a line from previous frame location of the pen to current frame position
    seg_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    seg_shape = pymunk.Segment(seg_body, previouspos, currentpos, LINE_WEIGHT)
    seg_shape.elasticity = 0.5
    space.add(seg_body, seg_shape)

    # x, y = x1, y1  # after drawing, the current position become previous position
    return seg_shape



def create_ball(sp, pos):
    body = pymunk.Body(1, 100)
    body.position = pos
    # body.mass = 1
    shape = pymunk.Circle(body, RAD)
    shape.elasticity = 0.1
    shape.friction = 0.5
    sp.add(body, shape)
    return shape


def draw_ball(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)

        pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), RAD)


def draw_path2(segments):
    for seg in segments:
        point1 = seg.a
        point2 = seg.b

        print("point1", point1)
        print("point2", point2)
        pygame.draw.line(screen, (0, 0, 0), point1, point2, LINE_WEIGHT)

# GROUP to draw
segs = []
balls = []
previouspos = (0,0)
currentpos = (0,0)
handState = 'None'
# MAIN GAME
def game():
    global previouspos, currentpos, handState
    clock = pygame.time.Clock()
    run = True
    while run:

        success, img = cap.read()
        img = cv2.flip(img, 1)
        img.flags.writeable = False
        img = detector.findHands(img, draw=False)
        lmList = detector.findPosition(img)

        if len(lmList) != 0:
            currentpos = lmList[8][1:]
            fingers = detector.fingersUp()

            if fingers[1] and fingers[2] == False:
                print("Draw")
                handState = "Drawing"
            if fingers[1] and fingers[2]:
                handState = "Selecting"
            if all(finger == False for finger in fingers):
                print("Close")
                handState = "Resting"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # RMB - CREATE BALL
        # Reset handstate will reset current position:
        if handState != "Drawing":
            previouspos = currentpos
        if handState == "Drawing":
            segs.append(create_segments(previouspos, currentpos))
            previouspos = currentpos
        # TAKE mouse position if pressed down
        if handState == "Creating":
            balls.append(create_ball(space, currentpos))
        screen.fill((247, 247, 247))
        draw_ball(balls)
        draw_path2(segs)

        space.step(DT)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)


game()
pygame.quit()
