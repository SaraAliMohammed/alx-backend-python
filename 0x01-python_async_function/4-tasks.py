#!/usr/bin/env python3
'''Module of task_wait_n function'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''It will spawn wait_random n times with the specified max_delay.
    Return the list of all the delays (float values).'''
    tasks = [task_wait_random(max_delay) for x in range(n)]
    times_list = await asyncio.gather(*tasks)
    return sorted(times_list)
