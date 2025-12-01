#!/usr/bin/env python3
"""Function that sums a list of floats with type annotations."""


def sum_list(input_list: list[float]) -> float:
    """Sum all the floats in a list.

    Args:
        input_list (list[float]): A list of floats to sum.

    Returns:
        float: The sum of all floats in the list.
    """
    return sum(input_list)
