#!/usr/bin/env python3
"""sum_list function"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function that returns the sum of floats

    Args:
        input_list (List[float]): List of float parameters

    Returns: Sum of the floats
    """
    total = 0
    for _ in range(len(input_list)):
        total += input_list[_]

    return total
