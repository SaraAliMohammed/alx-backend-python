#!/usr/bin/env python3
'''Module of an async routine called wait_n'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''It will spawn wait_random n times with the specified max_delay.
    Return the list of all the delays (float values).'''
    tasks = [wait_random(max_delay) for x in range(n)]
    times_list = await asyncio.gather(*tasks)
    return sorted(times_list)
