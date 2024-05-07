#!/usr/bin/env python3
""" Task 0 - Simple Helper Function """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ Creates a helper function to know what index series to show """
    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size

    return (start_index, end_index)
