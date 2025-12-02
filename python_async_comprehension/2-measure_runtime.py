#!/usr/bin/env python3
"""Run time for four parallel coroutines."""


import asyncio
import time

async_comprehension = __import__('1-concurrent_coroutines').wait_n

async def measure_runtime(n: int, max_delay: int) -> float:
    """Measure the total runtime of wait_n coroutine."""
    start_time = time.time()
    await async_comprehension(n, max_delay)
    end_time = time.time()
    return end_time - start_time
