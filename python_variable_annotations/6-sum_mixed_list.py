#!/usr/bin/env python3
""" Task 6 """

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ Returns the sum of a list of ints and floats """
    total: float = 0

    for item in mxd_list:
        total += item
    return total
