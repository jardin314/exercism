"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from
    'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the amount of time it will take to prepare the lasagna.

    :param number_of_layers: int - amount of layers in the lasagna.
    :return: int - amount of time it should take to prepare the given number of
    layers.

    Function that takes the number of layers in the lasagna as argument and
    returns how many minutes it takes to prepare that number of layers.
    """
    return number_of_layers*2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time
    :param number_of_layers: int - amount of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total amount of time elapsed

    Function that takes the number of layers in the lasagna, as well as
    the amount of time that has passed, and returns the total amount of
    time that has been spent on preparing the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
