#!/usr/bin/env python3
"""Module for basic asynchronous syntax demonstration."""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous function that waits for a random delay.

    Args:
        max_delay: The maximum delay in seconds (default is 10)
    Returns:
        The actual delay in seconds
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
