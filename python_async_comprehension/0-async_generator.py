#!/usr/bin/env python3
"""Coroutine that yields numbers asynchronously."""


import asyncio
import random

async def async_generator() -> int:
    """Asynchronous generator that yields numbers 0 to 9 with random delays."""
    for i in range(10):
        delay = random.uniform(0, 1)
        await asyncio.sleep(delay)
        yield i
