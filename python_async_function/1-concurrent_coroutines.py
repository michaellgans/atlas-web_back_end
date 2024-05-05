#!/usr/bin/env python3
""" Task 1 """

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns a list of all the delays """
    async_tasks = [wait_random(max_delay) for x in range(n)]
    delay_list = await asyncio.gather(*async_tasks)
    delay_list.sort()
    return delay_list
