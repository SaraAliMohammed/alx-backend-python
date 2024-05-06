#!/usr/bin/env python3
''' Module of asynchronous coroutine'''
import asyncio
import random


async def wait_random(max_delay: int = 10):
    '''
    Waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it.
    '''
    random_delay = random.random() * max_delay
    await asyncio.sleep(random_delay)
    return random_delay
