#!/usr/bin/env python3
"""concurrent coroutine"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Function takes two arguments and returns a list of all the delays
    [float values]

    Args:
        n (int): Number of times to run the delay Function
        max_delay (int): The maximum delay time in seconds

    Return:
        list[float]: The list of delays in ascending order without using sort()
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    return [delays[i] for i in range(n)]
