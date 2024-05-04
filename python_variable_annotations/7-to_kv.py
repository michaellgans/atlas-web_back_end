#!/usr/bin/env python3
""" Task 7 """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple from the variables inputted """
    v_squared: float = v * v
    return (k, v_squared)
