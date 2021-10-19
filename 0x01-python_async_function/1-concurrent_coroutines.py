#!/usr/bin/env python3
"""contains wait_n coroutine"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """calls wait_random n times"""
    wait_times: List[float] = []
    for f in asyncio.as_completed([wait_random(max_delay) for i in range(n)]):
        res = await f
        wait_times.append(res)
    return wait_times
