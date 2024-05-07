#!/usr/bin/env python3
'''Module of a coroutine called async_comprehension'''
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''The coroutine will collect 10 random numbers
    using an async comprehensing over async_generato,
    then return the 10 random numbers.'''
    result = [i async for i in async_generator()]
    return result
