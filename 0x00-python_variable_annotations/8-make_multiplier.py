#!/usr/bin/env python3
"""contains make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns function that multiplies a float by multiplier"""
    def func(multi: float) -> float:
        """returns product"""
        return multi * multiplier
    return func
