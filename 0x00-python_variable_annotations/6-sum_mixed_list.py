#!/usr/bin/env python3
"""sum_mixed_list function"""

from typing import List, Union

myType = Union[int, float]

def sum_mixed_list(mxd_lst: List[myType]) -> float:
    """
    Funtion that takes in a list of integers and floats and
    returns their sum

    Args:
        mxd_lst (Tuple[int, float, ...]): Tuple that contains ints and
        floats

    Returns: Sum of the tuple in float
    """
    total = 0
    for num in mxd_lst:
        if (isinstance(num, (int, float))):
            total += num

    return total
