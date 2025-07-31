#!/usr/bin/env python3
"""
This module contains an async routine that executes multiple coroutines concurrently.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return delays in ascending order.
    
    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay for each wait_random call
        
    Returns:
        List[float]: List of delays in ascending order without using sort()
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
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