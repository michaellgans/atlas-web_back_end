#!/usr/bin/env python3
""" Task 1 """

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns a list of all the delays """
    delay_list = []

    for x in range(n):
        delay_list.append(asyncio.create_task(wait_random(max_delay)))

    return [await delay_item for delay_item in asyncio.as_completed(delay_list)]
