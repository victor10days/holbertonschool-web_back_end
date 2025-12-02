#!/usr/bin/env python3
"""Multiple coroutines running concurrently."""


import asyncio
from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> list[float]:
    """Run wait_random n times concurrently and return the list of delays.

    Args:
        n: The number of coroutines to run
        max_delay: The maximum delay for each coroutine
    Returns:
        A list of delays from each coroutine
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays
