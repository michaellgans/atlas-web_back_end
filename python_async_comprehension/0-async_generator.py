#!/usr/bin/env python3
""" Task 0 """

import asyncio
import random


async def async_generator():
    """ Loops through 10 times and generates a random number """

    for x in range(10):
        await asyncio.sleep(1)
        number: float = random.uniform(0, 10)
        yield number
