#!/usr/bin/env python3
"""Measure runtime module."""
import asyncio
import time
from importlib import import_module

async_comprehension = import_module('1-async_comprehension')\
    .async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather and measures the total runtime.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
