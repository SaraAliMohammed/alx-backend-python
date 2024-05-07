#!/usr/bin/env python3
'''Module of a measure_runtime coroutine'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''It will execute async_comprehension
    four times in parallel using asyncio.gather.
    It should measure the total runtime and return it.'''
    start_time = time.time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    return time.time() - start_time
