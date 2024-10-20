#!/usr/bin/env python3
"""concurrent coroutine"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function takes two arguments and returns a list of all the delays
    [float values]

    Args:
        n (int): Number of times to run the delay Function
        max_delay (int): The maximum delay time in seconds

    Return:
        list[float]: The list of delays in *ascending order withoutusing
         using sort()*
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    return sorted(delays)
