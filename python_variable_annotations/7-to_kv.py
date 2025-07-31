#!/usr/bin/env python3
"""Module containing a type-annotated to_kv function."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with string k and square of v as float.
    
    Args:
        k: String key
        v: Integer or float value
        
    Returns:
        Tuple containing k and the square of v as a float
    """
    return (k, float(v ** 2))