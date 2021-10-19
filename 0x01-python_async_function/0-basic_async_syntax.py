#!/usr/bin/env python3
"""contains wait_random coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits and returns wait_time"""
    wait_time: float = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
