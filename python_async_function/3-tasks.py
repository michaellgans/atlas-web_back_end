#!/usr/bin/env python3
""" Task 3 """

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Returns an async task with a non async function """
    task = asyncio.get_event_loop()
    return task.create_task(wait_random(max_delay))
