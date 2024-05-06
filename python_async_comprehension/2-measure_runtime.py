#!/usr/bin/env python3
""" Task 2 """

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """ Runs async_comprehension """
    start_time: float = time.time()
    await asyncio.gather(*(async_comprehension() for x in range(4)))
    end_time: float = time.time()
    total_time: float = end_time - start_time
    return total_time
