#!/usr/bin/env python3
"""Module containing a type-annotated floor function."""
import math


def floor(n: float) -> int:
    """Return the floor of a float.
    
    Args:
        n: Float number to get the floor of
        
    Returns:
        The floor of n as an integer
    """
    return math.floor(n)
