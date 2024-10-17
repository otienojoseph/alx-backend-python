#!/usr/bin/python3
"""async coroutine"""

import asyncio
import random

async def wait_random(max_delay=10):
    """
    async function that takes in an integer argument and waits for a
    random delay between 0 max_delay seconds and eventually returns it.

    Args:
        max_delay: (int)
    Return - returns the max_delay
    """
    random_num = random.triangular(0, max_delay)
    await asyncio.sleep(random_num)
    return random_num
