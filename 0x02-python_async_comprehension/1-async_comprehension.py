#!/usr/bin/env python3
"""contains async_comprehension coroutine"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collects numbers from generator and returns them"""
    return [i async for i in async_generator()]
