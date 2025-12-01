#!/usr/bin/env python3
"""Function that returns a tuple as a key-value pair."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing a key-value pair.

    Args:
        k: The key as a string
        v: The value as an integer or float
    Returns:
        A tuple containing the key and the square of the value
    """
    return (k, float(v ** 2))
    