#!/usr/bin/env python3
"""Coroutine to measure runtime"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Function that measures the total execution time for wait_n

    Args:
        n (int): The number of times to run the Coroutine
        max_delay (int): The maximum delay time for execution
    Returns - The total_time / n
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time

    return (total_time / n)
