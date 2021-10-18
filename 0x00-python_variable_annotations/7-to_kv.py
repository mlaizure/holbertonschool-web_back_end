#!/usr/bin/env python3
"""contains to_kv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns tuple with k as 1st element and square of v as 2nd element"""
    return (k, v * v)
