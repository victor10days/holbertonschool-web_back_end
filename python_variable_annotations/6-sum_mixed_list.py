#!/usr/bin/env python3
"""Module containing a type-annotated sum_mixed_list function."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of integers and floats.
    
    Args:
        mxd_lst: List of integers and floats
        
    Returns:
        Sum of all numbers in the list as a float
    """
    return sum(mxd_lst)