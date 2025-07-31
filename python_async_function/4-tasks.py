#!/usr/bin/env python3
"""
This module contains task_wait_n function that uses asyncio Tasks.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create n asyncio Tasks and return delays in ascending order.

    Args:
        n (int): Number of tasks to create
        max_delay (int): Maximum delay for each task

    Returns:
        List[float]: List of delays in ascending order without using sort()
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    # Collect all results as they complete and maintain order naturally
    for task in asyncio.as_completed(tasks):
        delay = await task
        # Insert in proper position to maintain ascending order without sort()
        pos = 0
        while pos < len(delays) and delays[pos] < delay:
            pos += 1
        delays.insert(pos, delay)

    return delays
