from random import randint

INPUT_MODE = 'random'  # 'console' / 'auto' / 'random'

AUTO_POWER = 6
AUTO_DIRECTION = 0


def RANDOM_POWER(): return randint(4,7)


def RANDOM_DIRECTION(): return randint(-4,4)


STEP_RATE = 1/240.  # one spep lenght in seconds
DURATION = 2200     # steps of simulation with given STEP_RATE
TIME_BEFORE_FLING = 0.6

COCHONNET_RADIUS = 0.2
BALL_RADIUS = 0.4

BALL_MASS = 0.33
BALL_BOUNCENES = 0.6

PLANE_BOUNCENESS = 0.65
PLANE_LAT_FRIC = 0.2
PLANE_ROL_FRIC = 0

START_POSITION = (0, 0, 1)

BALLS_IN_ROUND = 1
ROUNDS_IN_GAME = 2
NUMBER_OF_PLAYERS = 2
