from random import uniform
from setup import *
from numpy import array

# auto vector for first fling
def random_cochonnete_vector():
    directory = (uniform(-1, 1)*600, uniform(-1, 1)*600, uniform(0.6, 0.8)*600)
    return directory


# brings little humanization
def randomize_vector(x, y, z):
    directory = (x * uniform(0.99, 1.1) / 3, y * uniform(0.99, 1.1) / 3, z * uniform(0.99, 1.1) / 3)
    return directory

# TODO get_start_position
def get_start_position():
    pass


# creates vector from input deviated from cochonnet direction -12: left, 0: straght, 12: right
def get_deviation_from_cachonnet(mode, cochonnet_place):
    x_coch = cochonnet_place[0]
    y_coch = cochonnet_place[1]
    z_coch = cochonnet_place[2]
    # manual input from console
    if mode == 'console':
        div = float(input('Choose the angle from cochonnetwise (-12: left, 0: straght, 12: right): '))
        # div should be -13 < x < 13
        if div >= 13:
            div = 12
        elif div <= -13:
            div = -12

        power = get_fling_power(mode) * 200
        return randomize_vector((x_coch - 0.6 * div) * power, (y_coch + 0.6 * div) * power, (z_coch + 6) * power)
    # auto generated input
    elif mode == 'auto':
        power = get_fling_power(mode)
        return  randomize_vector(x_coch * power, y_coch * power, (z_coch + 5) * power)


# gets fling power in range(0, 10), 5 is exact the same as cochonnet fling power
def get_fling_power(mode):
    # manual intut from console
    if mode =='console':
        x = float(input('Choose the power from 1 to 10: '))
        if x >= 10:
            return 2
        elif x > 0 and x < 11:
            return x/5
        elif x <= 1:
            return 1/5
    # auto generated input
    elif mode == 'auto':
        return POWER
