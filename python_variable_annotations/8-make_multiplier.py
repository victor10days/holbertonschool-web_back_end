#!/usr/bin/env python3
"""Function that returns multipliier of a float."""


def make_multiplier(multiplier: float) -> float:
    """Return a function that multiplies a float by the given multiplier.

    Args:
        multiplier: The multiplier as a float
    Returns:
        A function that multiplies a float by the multiplier
    """
    def multiply(n: float) -> float:
        """Multiply n by the multiplier.

        Args:
            n: The number to be multiplied
        Returns:
            The result of multiplying n by the multiplier
        """
        return n * multiplier

    return multiply
