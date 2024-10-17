#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

if __name__ == '__main__':
    s = time.perf_counter()
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
    end_time = time.perf_counter() - s
    print(f"The operation started at {s:0.2f} and has taken {end_time:0.2f} seconds.")
