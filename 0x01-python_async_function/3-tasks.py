#!/usr/bin/env python3
'''Module of task_wait_random function'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''It takes an integer max_delay and returns the created Task object.'''
    return asyncio.create_task(wait_random(max_delay))
