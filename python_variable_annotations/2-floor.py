#!/usr/bin/env python3
"""Module for flooring a float with type annotations."""


def floor(n: float) -> int:
    """Return the floor of a float as an integer.

    Args:
        n: The float number to floor
    Returns:
        The floored integer value
    """
    return int(n // 1)
