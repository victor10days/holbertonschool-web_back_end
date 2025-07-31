#!/usr/bin/env python3
"""Module containing a type-annotated sum_list function."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats.
    
    Args:
        input_list: List of float numbers
        
    Returns:
        Sum of all floats in the list
    """
    return sum(input_list)
