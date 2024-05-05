#!/usr/bin/env python3
""" Task 0 """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Waits based on a specific delay """
    wait_time: int = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
