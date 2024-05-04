#!/usr/bin/env python3
""" Task 8 """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function """
    def return_multiplier(number: float) -> float:
        """ Multiplies """
        return number * multiplier
    return return_multiplier
