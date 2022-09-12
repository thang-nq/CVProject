import os
import pygame,math
import pymunk
import GameObjects

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 900, 500
RAD = 20
LINE_WEIGHT = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")
space = pymunk.Space()
space.gravity = (0, 981)
x, y = 0, 0
collision = {"ball": 1, "goal": 2, "border": 3, "line": 4}
FPS = 60
VEL = 5
DT = 1 / FPS

# Add a new collision type
COLLTYPE_BALL = 2
COLLTYPE_GOAL = 3


# Define collision callback function, will be called when X touches Y
def goal_reached(arbiter, space, data):
    print("you reached the goal!")
    return True


# Setup the collision callback function
h = space.add_collision_handler(COLLTYPE_BALL, COLLTYPE_GOAL)
h.begin = goal_reached


# Create and add the "goal"
#
# def create_goal():
#     seg = GameObjects.Dot(space, RAD, (400, 200), collisionType="goal", color=(255, 0, 0), )
#     seg_shape = seg.shape
#     return seg


def create_dot(sp, pos):
    body = pymunk.Body(100, body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, LINE_WEIGHT)
    shape.elasticity = 1
    shape.friction = 0.5
    sp.add(body, shape)
    return shape


def create_apple(sp, pos):
    body = pymunk.Body(1, 100)
    body.position = pos
    # body.mass = 1
    shape = pymunk.Circle(body, RAD)
    shape.elasticity = 0.3
    shape.friction = 0.5
    sp.add(body, shape)
    return shape


def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)

        pygame.draw.circle(screen, apple.color, (pos_x, pos_y), RAD)


def draw_path(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)

        pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), LINE_WEIGHT)


def create_segments(pos):
    global x, y
    x1, y1 = pos

    # The drawing function will draw a line from 2 point
    if x == 0 and y == 0:  # if the pen is not inside the canvas or first start the app
        x, y = x1, y1  # pass the current coordinate of the pen
    else:  # draw a line from previous frame location of the pen to current frame position
        seg = GameObjects.Seg(space, 5, 1, (x, y), (x1, y1))
        seg_shape = seg.shape
        x, y = x1, y1  # after drawing, the current position become previous position
        return seg_shape


def draw_border(segments):
    global screen
    for seg in segments:
        point1 = seg.shape.a
        point2 = seg.shape.b

        pygame.draw.line(screen, (0, 0, 0), point1, point2, 5)


def draw_path2(segments):
    # x, y = x1, y1  # pass the current coordinate of the pen
    for seg in segments:
        point1 = seg.a
        point2 = seg.b

        pygame.draw.line(screen, (0, 0, 0), point1, point2, 5)


def draw_path_temp(segments):
    global screen
    # x, y = x1, y1  # pass the current coordinate of the pen
    for seg in segments:
        point1 = seg[0]
        point2 = seg[1]

        pygame.draw.line(screen, (0, 0, 0), point1, point2, 5)


def get_position(pos):
    global x, y, segs_coor
    x1, y1 = pos

    # The drawing function will draw a line from 2 point
    if x == 0 and y == 0:  # if the pen is not inside the canvas or first start the app
        x, y = x1, y1  # pass the current coordinate of the pen
    else:  # draw a line from previous frame location of the pen to current frame position
        # seg = GameObjects.Seg(self.space, 5, 1, (self.X, self.Y), (x1, y1))
        # seg_shape = seg.shape
        segs_coor.append(((x, y), (x1, y1)))
        x, y = x1, y1  # after drawing, the current position become previous position
        # return seg_shape


def create_segments2(segs_coor):
    global segs, space
    for seg in segs_coor:
        pos1 = seg[0]
        pos2 = seg[1]
        seg = GameObjects.Seg2(space, 5, 1, pos1, pos2)
        seg_shape = seg.shape
        segs.append(seg_shape)

def create_rect(space, pos, angle):
    body = pymunk.Body(1, 100, body_type= pymunk.Body.DYNAMIC)
    body.position = pos
    body.angle = angle
    poly_dims = [(-50, 0), (50, 0), (50, 5), (-50, 5)]
    shape = pymunk.Poly(body,poly_dims)
    space.add(body,shape)
    return shape

def drawShape(surf, color, shape):
    pts = []
    for v in shape.get_vertices():
        x, y = v.rotated(shape.body.angle) + shape.body.position
        pts.append((round(x), round(surf.get_width() - y)))
    pygame.draw.polygon(surf, color, pts, 2)


board = create_rect(space, (100, 100), math.pi / 4)
apples = []
dots = []
segs = []
segs_coor = []
border = []
platforms = []
border.append(
    GameObjects.Seg(space, 1, 1, (0, 0), (0, HEIGHT), elastic=0, collisionType="border"))
border.append(GameObjects.Seg(space, 1, 1, (0, HEIGHT), (WIDTH, HEIGHT), elastic=0,
                              collisionType="border"))
border.append(GameObjects.Seg(space, 1, 1, (WIDTH, HEIGHT), (WIDTH, 0), elastic=0,
                              collisionType="border"))
border.append(
    GameObjects.Seg(space, 1, 1, (WIDTH, 0), (0, 0), elastic=0, collisionType="border"))


# seg_body = pymunk.Body(body_type=pymunk.Body.STATIC)
# seg_shape = pymunk.Segment(seg_body, (100, 300), (450, 400), 1)
# seg_shape.elasticity = 0.5
# space.add(seg_body, seg_shape)


def game():
    clock = pygame.time.Clock()
    run = True
    board = create_rect(space, (100, 100), math.pi / 4)
    # goal = create_goal()
    gameStart = False
    player_img = pygame.image.load('MilkTeaImages/Bubble_Small.png').convert_alpha()
    while run:
        screen.fill((247, 247, 247))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # bubble = ball.Ball(space, RAD, 1)
                    # bubble.body.position = event.pos
                    #
                    # apples.append(create_apple(space,event.pos))
                    global x, y
                    x, y = pygame.mouse.get_pos()

                    # dots.append(create_dot(space, (x,y)))
                # elif event.button == 3:
                # apples.append(create_apple(space, event.pos))

                # dot = GameObjects.Dot(space, RAD, event.pos, COLLTYPE_BALL)
                # dots.append(draw_path(event.pos))
                if event.button == 3:
                    x, y = pygame.mouse.get_pos()
                    apples.append(GameObjects.Dot(space, 20,(x,y) , player_img,
                                    (20* 2.4, 20 * 2.4), 'ball'))
            if pygame.mouse.get_pressed()[0]:
                mpos = pygame.mouse.get_pos()

                # segs.append(create_segments(mpos))
                get_position(mpos)
                draw_path_temp(segs_coor)

            if event.type == pygame.MOUSEBUTTONUP:
                create_segments2(segs_coor)
                # apples.append(GameObjects.Dot(space, RAD, (200, 200), 'ball'))
                # apples.append(create_goal())
                platforms.append(GameObjects.Seg2(space, 5, 1, (100, 250), (300, 250), elastic=0).getShape())
                gameStart = True

        if not gameStart:
            pygame.draw.circle(screen, (0, 0, 0), (200, 200), RAD)
            pygame.draw.circle(screen, (255, 0, 0), (400, 200), RAD)

        # draw_goal(goal)
        draw_apples(apples)
        draw_path2(segs)
        draw_path2(platforms)
        drawShape(screen, (255, 255, 0), board)

        # space.debug_draw(draw_options)
        space.step(DT)

        pygame.display.update()
        # pygame.display.flip()
        clock.tick(FPS)


game()
pygame.quit()
