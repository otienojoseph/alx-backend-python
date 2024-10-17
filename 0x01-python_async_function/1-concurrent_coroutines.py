#!/usr/bin/env python3
"""concurrent coroutine"""

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
    delays = []

    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    return delays
