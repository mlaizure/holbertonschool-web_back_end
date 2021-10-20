#!/usr/bin/env python3
"""contains async_generator coroutine"""
import asyncio
import random


async def async_generator():
    """asynchronous generator for 10 random numbers that waits 1 sec between"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
