WIDTH = 1500
HEIGHT = 800

UI_STATES = {"main": 0, "levelSelect": 1, "setting": 2, "about": 3,
             "game": 4, "cleared": 5, "restart": 6, "lose": 7, "next": 8}

COLLISION_TYPES = {"ball": 1, "goal": 2, "border": 3, "die": 4, "line": 5}
LEVELS_SCORE = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DELAY = 300
FPS = 30
DT = 1 / FPS
GRAVITY = 500
PLAYER_RAD = 20
GOAL_RAD = 50
DEATH_RAD = 15
