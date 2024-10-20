#!/usr/bin/env python3
"""sum_mixed_list function"""

from typing import Tuple


def sum_mixed_list(mxd_lst: Tuple[int, float]) -> float:
    """
    Funtion that takes in a list of integers and floats and
    returns their sum

    Args:
        mxd_lst (Tuple[int, float, ...]): Tuple that contains ints and
        floats

    Returns: Sum of the tuple in float
    """
    total = 0
    for _ in range(len(mxd_lst)):
        total += mxd_lst[_]

    return total
