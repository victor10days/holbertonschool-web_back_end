#!/usr/bin/env python3
"""Function that sums a list of floats with type annotations.
Handles lists with mixed types (ints and floats).
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum all the numbers in a list containing both ints and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of ints and floats to sum.

    Returns:
        float: The sum of all numbers in the list.
    """
    return sum(mxd_lst)
