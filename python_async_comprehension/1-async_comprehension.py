#!/usr/bin/env python3
""" Task 1 """

import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ Runs async_generator """
    results = [result async for result in async_generator()]
    return results
