from random import uniform
from setup import *

# auto vector for first fling
def random_cochonnete_vector():
    power = AUTO_POWER/2
    directory = (uniform(-1, -0.5) * power, uniform(0.5, 1) * power, uniform(0.8, 0.9) * power)
    return directory


# brings little of humanization
def randomize_vector(x, y, z):
    directory = (x * uniform(0.99, 1.1), y * uniform(0.99, 1.1), z * uniform(0.99, 1.1))
    return directory


# check if the input in our range [min,max] and cut otherwise
def cut_input_by_range(input, min, max):
    if min <= input <= max:
        return input
    elif min > input:
        return min
    elif max < input:
        return max


# creates vector from input deviated from cochonnet direction -12: left, 0: straght, 12: right
def get_fling_vector(mode, cochonnet_place: tuple[float, float, float]) -> tuple[float, float, float]:
    x_coch = cochonnet_place[0]
    y_coch = cochonnet_place[1]
    z_coch = cochonnet_place[2]

    # manual input from console
    if mode == 'console':
        div = float(input('Choose the angle from cochonnetwise (-12: left, 0: straght, 12: right): '))
        # div should be -13 < x < 13
        div = cut_input_by_range(div, -12, 12)
        # if div >= 13:
        #     div = 12
        # elif div <= -13:
        #     div = -12

        power = get_fling_power(mode) / 12
        x_fling = (x_coch - 0.6 * div) * power
        y_fling = (y_coch + 0.6 * div) * power
        z_fling = (z_coch + 6) * power
        return randomize_vector(x_fling, y_fling, z_fling)
    # auto generated input
    elif mode == 'auto':
        div = AUTO_DIRECTION/7
        power = get_fling_power(mode) / 12

        x_fling = (x_coch + div) * power
        y_fling = (y_coch + div) * power
        z_fling = (z_coch + 1 + (x_coch**2 + y_coch**2)**0.5)

        return randomize_vector(x_fling, y_fling, z_fling)
    # random input
    elif mode == 'random':
        div = RANDOM_DIRECTION()
        power = get_fling_power(mode) / 12
        x_fling = (x_coch - 0.6 * div) * power
        y_fling = (y_coch + 0.6 * div) * power
        z_fling = z_coch + 1 + (x_coch**2 + y_coch**2)**0.5
        return randomize_vector(x_fling, y_fling, z_fling)


# gets fling power in range(0, 10), where 5 is exact the same as cochonnet fling power
def get_fling_power(mode):
    # manual intut from console
    if mode =='console':
        x = float(input('Choose the power from 1 to 10: '))
        # lets check if the input in our range
        return cut_input_by_range(x, 1, 10)
    # auto generated input
    elif mode == 'auto':
        return AUTO_POWER
    # random input
    elif mode == 'random':
        return RANDOM_POWER()

