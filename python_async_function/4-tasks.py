#!/usr/bin/env python3
""" Task 4 """

from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Duplicate task 1, but use task_wait_random """
    async_tasks = [task_wait_random(max_delay) for x in range(n)]

    return [await item for item in asyncio.as_completed(async_tasks)]
