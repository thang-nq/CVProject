import ball
import pygame
import pymunk
import pymunk.util as u
from pymunk import Vec2d

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 900, 500
RAD = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")
space = pymunk.Space()
space.gravity = (0, 981)

FPS = 60
VEL = 5
DT = 1 / FPS


def flipyv(self,v):
    return int(v.x), int(-v.y + h)

def convert_coordinate(point):
    return point[0], WIDTH - point[1]


def create_apple(sp, pos):
    body = pymunk.Body(1, 100)
    body.position = pos
    body.mass = 1
    shape = pymunk.Circle(body, RAD)
    shape.elasticity = 1
    shape.friction = 0.5
    sp.add(body, shape)
    return shape


def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)

        pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), RAD)


apples = []
seg_body = pymunk.Body(body_type=pymunk.Body.STATIC)
seg_shape = pymunk.Segment(seg_body, (100, 300), (450, 400), 1)
seg_shape.elasticity = 0.5
space.add(seg_body, seg_shape)


def game():
    clock = pygame.time.Clock()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                bubble = ball.Ball(space, RAD, 1)
                bubble.body.position = event.pos

                apples.append(bubble.shape)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    pass
            mpos = pygame.mouse.get_pos()

            if pygame.key.get_mods() & pygame.KMOD_SHIFT and pygame.mouse.get_pressed()[2]:
                p = self.flipyv(Vec2d(*mpos))
                self.poly_points.append(p)
            hit = self.space.point_query_nearest(
                self.flipyv(Vec2d(*mpos)), 0, pm.ShapeFilter()
            )
        screen.fill((247, 247, 247))
        pygame.draw.line(screen, (0, 0, 0), (100, 300), (450, 400), 1)
        draw_apples(apples)
        # draw_lines(screen, lines)

        # space.debug_draw(draw_options)

        space.step(DT)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)


game()
pygame.quit()
