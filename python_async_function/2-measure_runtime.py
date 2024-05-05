#!/usr/bin/env python3
""" Task 2 """

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 0) -> float:
    """ Records total wait time.  How to run an asyncio function """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    total_time: float = end_time - start_time
    return total_time / n
