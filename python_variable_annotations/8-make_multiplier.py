#!/usr/bin/env python3
"""Module containing a type-annotated make_multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier.
    
    Args:
        multiplier: Float multiplier value
        
    Returns:
        Function that multiplies a float by multiplier
    """
    def multiply(x: float) -> float:
        """Multiply x by the multiplier."""
        return x * multiplier
    
    return multiply
