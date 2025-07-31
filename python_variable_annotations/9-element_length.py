#!/usr/bin/env python3
"""Module containing a duck-typed element_length function."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing each element and its length.
    
    Args:
        lst: Iterable of sequences
        
    Returns:
        List of tuples where each tuple contains a sequence and its length
    """
    return [(i, len(i)) for i in lst]