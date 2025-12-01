#!/usr/bin/env python3
"""Function that sums a list of floats with type annotations.
Handles lists with mixed types (ints and floats).
"""


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    """Sum all the numbers in a list containing both ints and floats.

    Args:
        mxd_lst (list[int | float]): A list of integers and floats to sum.

    Returns:
        float: The sum of all numbers in the list.
    """
    return sum(mxd_lst)
