#!/usr/bin/env python3
"""async coroutine"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    async coroutine that waits for a random delay and returns it.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay that the function waited for.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
