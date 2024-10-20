#!/usr/bin/env python3
"""7-to_kv function"""

from typing import Tuple, Union

myType = Union[int, float]


def to_kv(k: str, v: myType) -> Tuple[str, myType]:
    """
    Function that takes string and an int OR float and returns Tuple

    Args:
        k (str): String parameter
        v (Tuple[int | float]): Tuple parameter of either int or float

    Returns: Tuple with first string and square of second parameter
    """

    newType: Tuple = (k, v**2)

    return newType
