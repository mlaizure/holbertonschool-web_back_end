#!/usr/bin/env python3
"""contains task_wait_n function"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """calls task_wait_random n times"""
    wait_times: List[float] = []
    for f in asyncio.as_completed([task_wait_random(max_delay)
                                   for i in range(n)]):
        res = await f
        wait_times.append(res)
    return wait_times
