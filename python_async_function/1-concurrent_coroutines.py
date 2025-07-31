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
    
    # Collect all results as they complete and maintain order naturally
    for task in asyncio.as_completed(tasks):
        delay = await task
        # Insert in proper position to maintain ascending order without sort()
        pos = 0
        while pos < len(delays) and delays[pos] < delay:
            pos += 1
        delays.insert(pos, delay)
    
    return delays