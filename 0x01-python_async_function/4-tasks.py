#!/usr/bin/env python3
"""4-tasks coroutine"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
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
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    return sorted(delays)
