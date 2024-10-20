#!/usr/bin/env python3
"""make_multiplier function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that multiplies a float by a given multiplier

    Args:
        multiplier (float): Float multiplier

    Returns: A funcion that multiplies a float by a multiplier
    """
    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
