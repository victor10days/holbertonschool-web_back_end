#!/usr/bin/env python3
"""Function to get element lengths with duck typing."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing elements and their lengths.

    Args:
        lst: An iterable of sequences

    Returns:
        A list of tuples, each containing a sequence and its length
    """
    return [(i, len(i)) for i in lst]
