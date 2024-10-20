#!/usr/bin/env python3
"""3-tasks function"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    task_wait_random - function that takes an integer and returns an
    `asyncio.Task`

    Args:
        max_delay (int): Max delay in seconds

    Return: An `asyncio.Task` object
    """
    return asyncio.create_task(wait_random(max_delay))
