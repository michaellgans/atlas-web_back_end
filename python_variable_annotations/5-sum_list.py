#!/usr/bin/env python3
""" Task 5 """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Returns the sum of a list of floats """
    total: float = 0
    for item in input_list:
        total += item
    return total
