#!/usr/bin/env python3
"""
This module contains task_wait_n function that uses asyncio Tasks.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create n asyncio Tasks using task_wait_random and return delays in ascending order.
    
    Args:
        n (int): Number of tasks to create
        max_delay (int): Maximum delay for each task
        
    Returns:
        List[float]: List of delays in ascending order without using sort()
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    
    # Use as_completed to get results as they finish, maintaining order naturally
    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        # Insert delay in the correct position to maintain ascending order
        inserted = False
        for i, existing_delay in enumerate(delays):
            if delay < existing_delay:
                delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            delays.append(delay)
    
    return delays