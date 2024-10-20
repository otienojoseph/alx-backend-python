#!/usr/bin/env python3
"""9-element_length annotation function"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    The function takes a list of elements (which can be of any type) and
    returns a list of tuples, where each tuple contains an element and
    its corresponding length.
    """
    return [(i, len(i)) for i in lst]
